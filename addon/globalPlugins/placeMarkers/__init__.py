# -*- coding: UTF-8 -*-
# placeMarkers: Plugin to manage place markers based on positions or strings in specific documents
# Copyright (C) 2012-2023 Noelia Ruiz Martínez, other contributors
# Released under GPL 2
# Converted to Python 3 by Joseph Lee in 2017
# UIA support added by Abdel in 2022

import pickle
import re
import os
import NVDAObjects
import UIAHandler
import shutil
import wx
from dataclasses import dataclass
from typing import Callable

import addonHandler
import globalPluginHandler
import appModuleHandler
import api
import globalVars
import textInfos
from textInfos.offsets import Offsets
from browseMode import BrowseModeDocumentTreeInterceptor
from NVDAObjects.UIA import chromium
import controlTypes
import gui
from gui import guiHelper
import core
import ui
import speech
from speech import sayAll
from scriptHandler import willSayAllResume, script
from logHandler import log

from .skipTranslation import translate

addonHandler.initTranslation()

_: Callable[[str], str]

# Constants
CONFIG_PATH = globalVars.appArgs.configPath
PLACE_MARKERS_PATH = os.path.join(
	CONFIG_PATH, "addons", "placeMarkers", "globalPlugins", "placeMarkers", "savedPlaceMarkers"
)
SEARCH_FOLDER = os.path.join(PLACE_MARKERS_PATH, "search")
BOOKMARKS_FOLDER = os.path.join(PLACE_MARKERS_PATH, "bookmarks")

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Globals
lastFindText = ""
lastCaseSensitivity = False


def goToUIABookmark(treeInterceptor: chromium.ChromiumUIATreeInterceptor, startOffset: int) -> bool:
	"""
	Allows to move the start browse mode textInfo endPoint
	to the location where the offset position passed in parameter is located,
	with Microsoft Edge, when UIA feature is enabled in NVDA advanced settings.
	The operation should be initiated from the position closest to the textInfo object
	@Parameters:
	@param treeInterceptor: The treeInterceptor object in which the move should occur.
	@type treeInterceptor: chromium.ChromiumUIATreeInterceptor.
	@param startOffset: The offset value towards which we want to perform the movement.
	@type startOffset: int.
	@returns: A boolean confirming the operation.
	@rtype: bool.
	"""
	focus = api.getFocusObject()
	allText = focus.makeTextInfo(textInfos.POSITION_ALL).text
	totalLength = len(allText)
	direction = "previous" if startOffset > totalLength / 2 else "next"
	# We store the position from which we want to start.
	if direction == "next":
		first = focus.treeInterceptor.makeTextInfo(textInfos.POSITION_FIRST)
		# We perform a first move with the MoveEndPointByUnit method.
		first._rangeObj.MoveEndpointByUnit(
			UIAHandler.TextPatternRangeEndpoint_End,
			UIAHandler.TextUnit_Character,
			startOffset
		)
		# As the move may not reach the correct offset, we make some adjustments.
		if len(first.text) > startOffset:
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_End,
				UIAHandler.TextUnit_Character,
				-(len(first.text) - startOffset)
			)
		if startOffset > len(first.text):
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_End,
				UIAHandler.TextUnit_Character,
				(startOffset - len(first.text))
			)
		if len(first.text) > startOffset:
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_End,
				UIAHandler.TextUnit_Character,
				-(len(first.text) - startOffset)
			)
		if startOffset > len(first.text):
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_End,
				UIAHandler.TextUnit_Character,
				(startOffset - len(first.text))
			)
	else:
		first = focus.treeInterceptor.makeTextInfo(textInfos.POSITION_LAST)
		startOffset = totalLength - startOffset
		# We perform a first move with the MoveEndPointByUnit method.
		first._rangeObj.MoveEndpointByUnit(
			UIAHandler.TextPatternRangeEndpoint_Start,
			UIAHandler.TextUnit_Character,
			- startOffset
		)
		# As the move may not reach the correct offset, we make some adjustments.
		if len(first.text) > startOffset:
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_Start,
				UIAHandler.TextUnit_Character,
				(len(first.text) - startOffset)
			)
		if startOffset > len(first.text):
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_Start,
				UIAHandler.TextUnit_Character,
				-(startOffset - len(first.text))
			)
		if len(first.text) > startOffset:
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_Start,
				UIAHandler.TextUnit_Character,
				(len(first.text) - startOffset)
			)
		if startOffset > len(first.text):
			first._rangeObj.MoveEndpointByUnit(
				UIAHandler.TextPatternRangeEndpoint_Start,
				UIAHandler.TextUnit_Character,
				-(startOffset - len(first.text))
			)
	if len(first.text) == startOffset:
		if direction == "previous":
			first.collapse()
		else:
			first.collapse(True)
		treeInterceptor._set_selection(first)
		info = treeInterceptor.selection
		info.expand(textInfos.UNIT_WORD)
		speech.speakTextInfo(info, reason=controlTypes.OutputReason.CARET)
		info.collapse()
		return True
	return False


def goToNonUIABookmark(obj, position):
	bookmark = Offsets(position, position)
	info = obj.makeTextInfo(bookmark)
	obj._set_selection(info)
	speech.cancelSpeech()
	info.move(textInfos.UNIT_LINE, 1, endPoint="end")
	speech.speakTextInfo(info, reason=controlTypes.OutputReason.CARET)


def disableInSecureMode(decoratedCls):
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls


def createSearchFolder():
	if os.path.isdir(SEARCH_FOLDER):
		return
	try:
		os.makedirs(SEARCH_FOLDER)
	except Exception as e:
		log.debugWarning("Error creating search folder", exc_info=True)
		raise e


def createBookmarksFolder():
	if os.path.isdir(BOOKMARKS_FOLDER):
		return
	try:
		os.makedirs(BOOKMARKS_FOLDER)
	except Exception as e:
		log.debugWarning("Error creating bookmarks folder", exc_info=True)
		raise e


createSearchFolder()
createBookmarksFolder()


def doFindText(text, reverse=False, caseSensitive=False, willSayAllResume=False):
	if not text:
		return
	obj = api.getFocusObject()
	treeInterceptor = obj.treeInterceptor
	if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
		obj = treeInterceptor
		obj.doFindText(text=text, reverse=reverse, caseSensitive=caseSensitive, willSayAllResume=willSayAllResume)
	elif obj.role != controlTypes.Role.EDITABLETEXT:
		return
	else:
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
		except(NotImplementedError, RuntimeError):
			info = obj.makeTextInfo(textInfos.POSITION_FIRST)
		try:
			res = info.find(text, reverse=reverse, caseSensitive=caseSensitive)
		except WindowsError:
			wx.CallAfter(
				gui.messageBox,
				# Message translated in NVDA core.
				translate('text "%s" not found') % text,
				# Message translated in NVDA core.
				translate("Find Error"),
				wx.OK | wx.ICON_ERROR
			)
		except Exception:
			if api.copyToClip(text):
				# Translators: message presented when a string of text has been copied to the clipboard.
				ui.message(_("%s copied to clipboard") % text)
			return
		if res:
			if hasattr(obj, 'selection'):
				obj.selection = info
			else:
				info.updateCaret()
			speech.cancelSpeech()
			info.move(textInfos.UNIT_LINE, 1, endPoint="end")
			speech.speakTextInfo(info, reason=controlTypes.OutputReason.CARET)
		else:
			wx.CallAfter(
				gui.messageBox,
				# Message translated in NVDA core.
				translate('text "%s" not found') % text,
				# Message translated in NVDA core.
				translate("Find Error"),
				wx.OK | wx.ICON_ERROR
			)


def doFindTextUp(text, caseSensitive=False, willSayAllResume=False):
	doFindText(text, reverse=True, caseSensitive=caseSensitive, willSayAllResume=willSayAllResume)


def moveToBookmark(position):
	obj = api.getFocusObject()
	treeInterceptor = obj.treeInterceptor
	if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
		obj = treeInterceptor
		if (
			isinstance(obj, chromium.ChromiumUIATreeInterceptor)
			or isinstance(obj, UIAHandler.browseMode.UIADocumentWithTableNavigation)
		):
			goToUIABookmark(obj, position)
		else:
			goToNonUIABookmark(obj, position)


def standardFileName(fileName):
	notAllowed = re.compile(r"\?|:|\*|\t|<|>|\"|\/|\\||")  # Invalid characters
	allowed = re.sub(notAllowed, "", fileName)
	return allowed


def getFile(folder, ext=""):
	rootObj = None
	treeInterceptor = None
	obj = api.getForegroundObject()
	file = obj.name
	uia = False
	obj = api.getFocusObject()
	if (
		obj and obj.treeInterceptor
		and isinstance(obj.treeInterceptor, BrowseModeDocumentTreeInterceptor)
		and not obj.treeInterceptor.passThrough
	):
		treeInterceptor = obj.treeInterceptor
		rootObj = obj.treeInterceptor.rootNVDAObject
		if rootObj and isinstance(rootObj, NVDAObjects.IAccessible.IAccessible):
			uia = False
			childID = rootObj.IAccessibleChildID
			iAObj = rootObj.IAccessibleObject
			val = iAObj.accValue(childID)
		if rootObj and treeInterceptor and isinstance(treeInterceptor, chromium.ChromiumUIATreeInterceptor):
			uia = True
			val = rootObj.UIAValuePattern.CurrentValue
		try:
			nameToAdd = " - %s" % val.split("#")[0].split("/")[-1].split("\\")[-1]
		except Exception:
			nameToAdd = ""
	else:
		nameToAdd = ""
	file = file.rsplit(" - ", 1)[0]
	file = file.split("\\")[-1]
	file = f"uia_{file}" if uia else file
	file += nameToAdd
	file = api.filterFileName(standardFileName(file))
	folderPath = os.path.join(PLACE_MARKERS_PATH, folder)
	maxLenFileName = 232 - len(folderPath)
	if maxLenFileName <= 0:
		return ""
	file = file[:maxLenFileName]
	file = file + ext
	path = os.path.join(folderPath, file)
	return path


def getFileSearch():
	return getFile("search", ".txt")


def getSavedTexts():
	searchFile = getFileSearch()
	try:
		with open(searchFile, "r", encoding="utf-8") as f:
			savedStrings = f.read().split("\n")
	except Exception:
		savedStrings = []
	return savedStrings


def getLastSpecificFindText():
	try:
		return getSavedTexts()[0]
	except Exception:
		return ""


def getFileBookmarks():
	return getFile("bookmarks", ".pickle")


def getFileTempBookmark():
	return getFile("bookmarks", ".txt")


def getSavedBookmarks():
	fileName = getFileBookmarks()
	try:
		with open(fileName, "rb") as f:
			savedBookmarks = pickle.load(f)
		if isinstance(savedBookmarks, list):
			bookmarksDic = {}
			for bookmark in savedBookmarks:
				bookmarksDic[bookmark] = Note()
			savedBookmarks = bookmarksDic
	except IOError:
		savedBookmarks = {}
	return savedBookmarks


# Dialogs

class SpecificSearchDialog(wx.Dialog):

	def __init__(self, parent, reverse=False):
		# Translators: The title of the Specific Search dialog.
		super(SpecificSearchDialog, self).__init__(parent, title=_("Specific search"))
		self.searchFile = getFileSearch()
		self.savedTexts = getSavedTexts()
		self.reverse = reverse
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: The label of a combo box in the Specific Search dialog.
		savedTextsLabel = _("Sa&ved texts")
		self.savedTextsComboBox = sHelper.addLabeledControl(savedTextsLabel, wx.Choice, choices=self.savedTexts)
		self.savedTextsComboBox.Bind(wx.EVT_CHOICE, self.onSavedTextsChange)
		# Translators: A label for a chekbox in the Specific search dialog.
		self.removeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Remove from history")))
		self.removeCheckBox.Disable()
		# Translators: The label of an edit box in the Specific Search dialog.
		searchTextLabel = _("&Text to search:")
		self.searchTextEdit = sHelper.addLabeledControl(searchTextLabel, wx.TextCtrl)
		self.searchTextEdit.Value = getLastSpecificFindText()
		self.searchTextEdit.Bind(wx.EVT_TEXT, self.onSearchEditTextChange)
		# Translators: A label for a chekbox in the Specific search dialog.
		self.addCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Add to history")))
		# Translators: Label for a set of radio buttons in the Specific search dialog.
		searchActionsLabel = _("Action on s&earch")
		searchChoices = (
			# Translators: An action in the Search group of the Specific search dialog.
			_("Search &next"),
			# Translators: An action in the Search group of the Specific search dialog.
			_("Search &previous"),
			# Translators: An action in the Search group of the Specific search dialog.
			_("&Don't search"),
		)
		self.searchRadioBox = sHelper.addItem(wx.RadioBox(self, label=searchActionsLabel, choices=searchChoices))
		if self.reverse:
			self.searchRadioBox.SetSelection(1)
		self.searchRadioBox.Bind(wx.EVT_RADIOBOX, self.onSearchRadioBox)
		# Message translated in NVDA core.
		self.caseSensitiveCheckBox = sHelper.addItem(wx.CheckBox(self, label=translate("Case &sensitive")))
		self.caseSensitiveCheckBox.Value = lastCaseSensitivity
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.searchTextEdit.SetFocus()
		if not self.searchTextEdit.Value:
			self.addCheckBox.Disable()
			self.searchRadioBox.Disable()
			self.caseSensitiveCheckBox.Disable()
		self.CentreOnScreen()

	def onSearchEditTextChange(self, evt):
		if self.searchTextEdit.Value:
			self.addCheckBox.Enable()
			self.searchRadioBox.Enable()
			self.caseSensitiveCheckBox.Enable()
		else:
			self.addCheckBox.Disable()
			self.searchRadioBox.Disable()
			self.caseSensitiveCheckBox.Disable()

	def onSavedTextsChange(self, evt):
		self.searchTextEdit.Value = self.savedTextsComboBox.GetStringSelection()
		self.removeCheckBox.Enable()

	def onSearchRadioBox(self, evt):
		if self.searchRadioBox.Selection == 2:  # Don't search
			self.caseSensitiveCheckBox.Disable()

	def onOk(self, evt):
		self.Destroy()
		if self.addCheckBox.Value or self.searchRadioBox.Selection < 2:  # Add or search
			text = self.searchTextEdit.Value
		actionToPerform = self.searchRadioBox.Selection
		if actionToPerform < 2:  # Search
			caseSensitive = self.caseSensitiveCheckBox.Value
			if actionToPerform == 0:
				core.callLater(1000, doFindText, text, caseSensitive=caseSensitive)
			else:
				core.callLater(1000, doFindTextUp, text, caseSensitive=caseSensitive)
			global lastFindText, lastCaseSensitivity
			lastFindText = text
			lastCaseSensitivity = caseSensitive
		if self.addCheckBox.Value or self.removeCheckBox.Value:
			savedStrings = self.savedTexts
			if self.removeCheckBox.Value:
				del savedStrings[self.savedTextsComboBox.Selection]
			if self.addCheckBox.Value and "\n" not in text and text not in savedStrings:
				savedStrings.insert(0, text)
			if len(savedStrings) == 0:
				os.remove(self.searchFile)
				return
			try:
				with open(self.searchFile, "w", encoding="utf-8") as f:
					f.write("\n".join(savedStrings))
			except Exception as e:
				log.debugWarning("Error saving strings of text for specific search", exc_info=True)
				raise e


def doCopy(copyDirectory):
	# Borrowed from @ibrahim-s code for readFeeds in PR#4
	# to ensure that the removed directory will not be one of the main directories such as documents or music
	# or other important ones
	if not os.path.basename(copyDirectory) == "placeMarkersBackup":
		copyDirectory = os.path.join(copyDirectory, "placeMarkersBackup")
	try:
		if os.path.exists(copyDirectory):
			# if it exists, only placeMarkersBackup folder will be removed,
			# which is the base name of copyDirectory path
			shutil.rmtree(copyDirectory, ignore_errors=True)
		shutil.copytree(PLACE_MARKERS_PATH, copyDirectory)
		core.callLater(
			100, ui.message,
			# Translators: Message presented when place markers have been copied.
			_("Place markers copied")
		)
	except Exception as e:
		wx.CallAfter(
			gui.messageBox,
			# Translators: label of error dialog shown when cannot copy placeMarkers folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy placeMarkers folder.
			_("Copy Error"),
			wx.OK | wx.ICON_ERROR
		)
		raise e


def doRestore(restoreDirectory):
	try:
		shutil.rmtree(PLACE_MARKERS_PATH, ignore_errors=True)
		shutil.copytree(restoreDirectory, PLACE_MARKERS_PATH)
		core.callLater(
			100, ui.message,
			# Translators: Message presented when place markers have been restored.
			_("Place markers restored")
		)
	except Exception as e:
		wx.CallAfter(
			gui.messageBox,
			# Translators: label of error dialog shown when cannot copy placeMarkers folder.
			_("Folder not copied"),
			# Translators: title of error dialog shown when cannot copy placeMarkers folder.
			_("Copy Error"),
			wx.OK | wx.ICON_ERROR
		)
		raise e


class NotesDialog(wx.Dialog):

	def __init__(self, parent, fileName):
		# Translators: The title of the Notes dialog.
		super(NotesDialog, self).__init__(parent, title=_("Notes"))
		self.fileName = fileName
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: The label of a list box in the Notes dialog.
		notesLabel = _("&Bookmarks")
		self.bookmarks = getSavedBookmarks()
		positions = sorted(self.bookmarks)
		self.pos = positions[0]
		firstNoteBody = self.bookmarks[self.pos].body
		notesChoices = []
		for pos in positions:
			notesChoices.append("{position} - {title}".format(position=pos, title=self.bookmarks[pos].title))
		self.notesListBox = sHelper.addLabeledControl(notesLabel, wx.ListBox, choices=notesChoices)
		self.notesListBox.Selection = 0
		self.notesListBox.Bind(wx.EVT_LISTBOX, self.onNotesChange)
		# Translators: The label of an edit box in the Notes dialog.
		noteLabel = _("Not&e:")
		noteLabeledCtrl = gui.guiHelper.LabeledControlHelper(self, noteLabel, wx.TextCtrl, style=wx.TE_MULTILINE)
		self.noteEdit = noteLabeledCtrl.control
		self.noteEdit.SetMaxLength(1024)
		self.noteEdit.Value = firstNoteBody
		bHelper = sHelper.addItem(guiHelper.ButtonHelper(orientation=wx.HORIZONTAL))
		# Translators: The label for a button in the Notes dialog.
		self.saveButton = bHelper.addButton(self, label=_("&Save note"))
		self.Bind(wx.EVT_BUTTON, self.onSave, self.saveButton)
		# Translators: The label for a button in the Notes dialog.
		self.deleteButton = bHelper.addButton(self, label=_("&Delete..."))
		self.deleteButton.Bind(wx.EVT_BUTTON, self.onDelete)
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.notesListBox.SetFocus()
		self.CentreOnScreen()

	def onNotesChange(self, evt):
		self.pos = int(self.notesListBox.GetStringSelection().split(" - ")[0])
		self.noteEdit.Value = self.bookmarks[self.pos].body

	def onSave(self, evt):
		noteTitle = self.notesListBox.GetStringSelection().split(" - ")[1]
		noteBody = self.noteEdit.Value
		note = Note(noteTitle, noteBody)
		self.bookmarks[self.pos] = note
		try:
			with open(self.fileName, "wb") as f:
				pickle.dump(self.bookmarks, f, protocol=0)
			self.notesListBox.SetFocus()
		except Exception as e:
			log.debugWarning("Error saving bookmark", exc_info=True)
			raise e

	def onDelete(self, evt):
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a bookmark.
			_("This bookmark will be permanently deleted. This action cannot be undone."),
			# Message translated in NVDA core.
			translate("Confirm Deletion"),
			wx.OK | wx.CANCEL | wx.ICON_QUESTION, self
		) != wx.OK:
			return
		del self.bookmarks[self.pos]
		if len(self.bookmarks.keys()) > 0:
			try:
				with open(self.fileName, "wb") as f:
					pickle.dump(self.bookmarks, f, protocol=0)
				self.notesListBox.Delete(self.notesListBox.Selection)
				self.notesListBox.Selection = 0
				self.onNotesChange(None)
				self.notesListBox.SetFocus()
			except Exception as e:
				log.debugWarning("Error deleting bookmark", exc_info=True)
				raise e
		else:
			try:
				os.remove(self.fileName)
				self.Destroy()
				wx.CallAfter(
					gui.messageBox,
					# Translators: The message presented when all bookmarks have been deleted from the Notes dialog.
					_("No bookmarks"),
					# Translators: The title of the warning dialog when all bookmarks have been deleted.
					_("Bookmarks deleted"),
					wx.OK | wx.ICON_WARNING, None
				)
			except WindowsError:
				pass

	def onOk(self, evt):
		self.Destroy()
		core.callLater(1000, moveToBookmark, self.pos)


class CopyDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Copy dialog.
		super(CopyDialog, self).__init__(parent, title=_("Copy place markers"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Copy dialog.
		dialogCaption = _("Select a folder to save a backup of your current place markers.")
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping with controls to select the destination directory in the Copy dialog.
		directoryGroupText = _("directory for backup:")
		groupHelper = sHelper.addItem(
			gui.guiHelper.BoxSizerHelper(
				self, sizer=wx.StaticBoxSizer(wx.StaticBox(
					self, label=directoryGroupText), wx.VERTICAL
				)
			)
		)
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog to browse for the destination directory when copying place markers.
		dirDialogTitle = _("Select directory to copy")
		directoryEntryControl = groupHelper.addItem(
			gui.guiHelper.PathSelectionHelper(self, browseText, dirDialogTitle)
		)
		self.copyDirectoryEdit = directoryEntryControl.pathControl
		self.copyDirectoryEdit.Value = os.path.join(CONFIG_PATH, "placeMarkersBackup")
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		# Message translated in NVDA core.
		continueButton = bHelper.addButton(self, label=translate("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onCopy)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.CentreOnScreen()

	def onCopy(self, evt):
		if not self.copyDirectoryEdit.Value:
			# Message translated in NVDA core.
			gui.messageBox(
				translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		drv = os.path.splitdrive(self.copyDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Message translated in NVDA core.
			gui.messageBox(
				translate("Invalid drive %s") % drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		self.Hide()
		doCopy(self.copyDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()


class PathSelectionWithoutNewDir(gui.guiHelper.PathSelectionHelper):

	def __init__(self, parent, buttonText, browseForDirectoryTitle):
		super(PathSelectionWithoutNewDir, self).__init__(parent, buttonText, browseForDirectoryTitle)

	def onBrowseForDirectory(self, evt):
		startPath = self.getDefaultBrowseForDirectoryPath()
		with wx.DirDialog(
			self._parent, self._browseForDirectoryTitle,
			defaultPath=startPath, style=wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE
		) as d:
			if d.ShowModal() == wx.ID_OK:
				self._textCtrl.Value = d.Path


class RestoreDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Restore dialog.
		super(RestoreDialog, self).__init__(parent, title=_("Restore place markers"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Restore dialog.
		dialogCaption = _("Select a folder to restore a backup of your previous copied place markers.")
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping with controls to select the destination directory in Restore dialog.
		directoryGroupText = _("directory containing backup:")
		groupHelper = sHelper.addItem(
			gui.guiHelper.BoxSizerHelper(
				self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)
			)
		)
		# Message translated in NVDA core.
		browseText = translate("Browse...")
		# Translators: The title of the dialog to browse for the destination directory when restoring place markers.
		dirDialogTitle = _("Select directory to restore")
		directoryEntryControl = groupHelper.addItem(PathSelectionWithoutNewDir(self, browseText, dirDialogTitle))
		self.restoreDirectoryEdit = directoryEntryControl.pathControl
		backupDirectory = os.path.join(CONFIG_PATH, "placeMarkersBackup")
		if os.path.isdir(backupDirectory):
			self.restoreDirectoryEdit.Value = backupDirectory
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		# Message translated in NVDA core.
		continueButton = bHelper.addButton(self, label=translate("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onRestore)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.CentreOnScreen()

	def onRestore(self, evt):
		if not self.restoreDirectoryEdit.Value:
			# Message translated in NVDA core.
			gui.messageBox(
				translate("Please specify a directory."),
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		drv = os.path.splitdrive(self.restoreDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Message translated in NVDA core.
			gui.messageBox(
				translate("Invalid drive %s") % drv,
				# Message translated in NVDA core.
				translate("Error"),
				wx.OK | wx.ICON_ERROR
			)
			return
		self.Hide()
		doRestore(self.restoreDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()


# Note

@dataclass
class Note:
	title: str = ""
	body: str = ""


# Global plugin

@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.BSMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(
			self.BSMenu,
			# Translators: the name of addon submenu.
			_("P&lace markers"),
			# Translators: the tooltip text for addon submenu.
			_("Bookmarks and Search menu")
		)
		self.searchItem = self.BSMenu.Append(
			wx.ID_ANY,
			# Translators: the name for an item of addon submenu.
			_("&Specific search folder"),
			# Translators: the tooltip text for an item of addon submenu.
			_("Opens the specific search folder")
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSpecificSearch, self.searchItem)
		self.bookmarksItem = self.BSMenu.Append(
			wx.ID_ANY,
			# Translators: the name for an item of addon submenu.
			_("&Bookmarks folder"),
			# Translators: the tooltip text for an item of addon submenu.
			_("Opens the bookmarks folder")
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onBookmarks, self.bookmarksItem)
		self.copyItem = self.BSMenu.Append(
			wx.ID_ANY,
			# Translators: the name for an item of addon submenu.
			_("&Copy placeMarkers folder..."),
			# Translators: the tooltip text for an item of addon submenu.
			_("Backup of place markers")
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCopy, self.copyItem)
		self.restoreItem = self.BSMenu.Append(
			wx.ID_ANY,
			# Translators: the name for an item of addon submenu.
			_("R&estore place markers..."),
			# Translators: the tooltip text for an item of addon submenu.
			_("Restore previously saved place markers")
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onRestore, self.restoreItem)

	def terminate(self):
		try:
			self.menu.Remove(self.mainItem)
		except Exception:
			pass

	def onSpecificSearch(self, evt):
		os.startfile(SEARCH_FOLDER)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Opens the specific search folder.")
	)
	def script_openSpecificSearchFolder(self, gesture):
		wx.CallAfter(self.onSpecificSearch, None)

	def onBookmarks(self, evt):
		os.startfile(BOOKMARKS_FOLDER)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Opens the bookmarks folder.")
	)
	def script_openBookmarksFolder(self, gesture):
		wx.CallAfter(self.onBookmarks, None)

	def onCopy(self, evt):
		gui.mainFrame.prePopup()
		d = CopyDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Activates the Copy dialog of %s.") % ADDON_SUMMARY
	)
	def script_activateCopyDialog(self, gesture):
		wx.CallAfter(self.onCopy, None)

	def onRestore(self, evt):
		gui.mainFrame.prePopup()
		d = RestoreDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Activates the Restore dialog of %s.") % ADDON_SUMMARY
	)
	def script_activateRestoreDialog(self, gesture):
		wx.CallAfter(self.onRestore, None)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("finds a text string from the current cursor position for a specific document."),
		gesture="kb:NVDA+control+shift+f"
	)
	def script_specificFind(self, gesture, reverse=False):
		obj = api.getFocusObject()
		if controlTypes.State.MULTILINE not in obj.states:
			treeInterceptor = obj.treeInterceptor
			if not(isinstance(
				treeInterceptor, BrowseModeDocumentTreeInterceptor
			) and not treeInterceptor.passThrough):
				gesture.send()
				return

		# Adapted from Joseph Lee's work in NVDA's core
		# #8566: We need this to be a modal dialog, but it mustn't block this script.
		def run():
			gui.mainFrame.prePopup()
			d = SpecificSearchDialog(gui.mainFrame, reverse=reverse)
			d.ShowModal()
			gui.mainFrame.postPopup()
		wx.CallAfter(run)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("finds the next occurrence of the last text searched for any specific document."),
		resumeSayAllMode=sayAll.CURSOR.CARET,
	)
	def script_specificFindNext(self, gesture):
		obj = api.getFocusObject()
		if controlTypes.State.MULTILINE not in obj.states:
			treeInterceptor = obj.treeInterceptor
			if not(
				isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough
			):
				gesture.send()
				return
		if not lastFindText:
			self.script_specificFind(gesture)
		else:
			doFindText(
				lastFindText,
				lastCaseSensitivity,
				willSayAllResume=willSayAllResume(gesture),
			)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("finds the previous occurrence of the last text searched for any specific document."),
		resumeSayAllMode=sayAll.CURSOR.CARET,
	)
	def script_specificFindPrevious(self, gesture):
		obj = api.getFocusObject()
		if controlTypes.State.MULTILINE not in obj.states:
			treeInterceptor = obj.treeInterceptor
			if not(
				isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough
			):
				gesture.send()
				return
		if not lastFindText:
			self.script_specificFind(gesture, reverse=True)
		else:
			doFindTextUp(
				lastFindText,
				lastCaseSensitivity,
				willSayAllResume=willSayAllResume(gesture),
			)

	def popupNotesDialog(self):
		if getSavedBookmarks() == {}:
			ui.message(
				# Translators: message presented when the current document doesn't contain bookmarks.
				_("No bookmarks")
			)
			return
		gui.mainFrame.prePopup()
		d = NotesDialog(gui.mainFrame, getFileBookmarks())
		d.Show()
		gui.mainFrame.postPopup()

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Show the Notes dialog for a specific document."),
		gesture="kb:NVDA+alt+y"
	)
	def script_activateNotesDialog(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if not (
			isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor)
			and not treeInterceptor.passThrough
		):
			gesture.send()
			return
		wx.CallAfter(self.popupNotesDialog)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Saves the current position as a bookmark."),
		gesture="kb:NVDA+control+shift+y"
	)
	def script_saveBookmark(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		# Code for UIA provided by Abdel(@abdel792)
		if (
			isinstance(treeInterceptor, chromium.ChromiumUIATreeInterceptor)
			or isinstance(treeInterceptor, UIAHandler.browseMode.UIADocumentWithTableNavigation)
		):
			first = obj.makeTextInfo(textInfos.POSITION_FIRST)
			cur = obj.selection
			first.setEndPoint(cur, "endToStart")
			startOffset = len(first.text)
		else:
			bookmark = obj.makeTextInfo(textInfos.POSITION_CARET).bookmark
			startOffset = bookmark.startOffset
		bookmarks = getSavedBookmarks()
		noteTitle = obj.makeTextInfo(textInfos.POSITION_SELECTION).text[:100]
		if startOffset in bookmarks:
			noteBody = bookmarks[startOffset].body
		else:
			noteBody = ""
		bookmarks[startOffset] = Note(noteTitle, noteBody)
		fileName = getFileBookmarks()
		try:
			with open(fileName, "wb") as f:
				pickle.dump(bookmarks, f, protocol=0)
			ui.message(
				# Translators: message presented when a position is saved as a bookmark.
				_("Saved position at character %d") % startOffset
			)
		except Exception as e:
			log.debugWarning("Error saving bookmark", exc_info=True)
			ui.message(
				# Translators: message presented when a bookmark cannot be saved.
				_("Cannot save bookmark")
			)
			raise e

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Deletes the current bookmark."),
		gesture="kb:NVDA+control+shift+delete"
	)
	def script_deleteBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		bookmarks = getSavedBookmarks()
		if bookmarks == {}:
			ui.message(
				# Translators: message presented when the current document doesn't contain bookmarks.
				_("No bookmarks")
			)
			return
		if isinstance(treeInterceptor, chromium.ChromiumUIATreeInterceptor):
			first = obj.makeTextInfo(textInfos.POSITION_FIRST)
			cur = obj.selection
			first.setEndPoint(cur, "endToStart")
			startOffset = len(first.text)
		else:
			bookmark = obj.makeTextInfo(textInfos.POSITION_CARET).bookmark
			startOffset = bookmark.startOffset
		if startOffset not in bookmarks:
			ui.message(
				# Translators: message presented when the current document has bookmarks, but none is selected.
				_("No bookmark selected")
			)
			return
		del(bookmarks[startOffset])
		fileName = getFileBookmarks()
		if bookmarks != {}:
			try:
				with open(fileName, "wb") as f:
					pickle.dump(bookmarks, f, protocol=0)
				ui.message(
					# Translators: message presented when a bookmark is deleted.
					_("Bookmark deleted")
				)
				return
			except Exception:
				pass
		else:
			try:
				os.remove(fileName)
				ui.message(
					# Translators: message presented when the current document doesn't contain bookmarks.
					_("No bookmarks")
				)
				return
			except WindowsError:
				pass
		log.debugWarning("Error saving bookmarks", exc_info=True)
		ui.message(
			# Translators: message presented when cannot delete a bookmark.
			_("Cannot delete bookmark")
		)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Moves to the next bookmark."),
		resumeSayAllMode=sayAll.CURSOR.CARET,
		gesture="kb:NVDA+y"
	)
	def script_selectNextBookmark(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		bookmarks = getSavedBookmarks()
		if bookmarks == {}:
			ui.message(
				# Translators: message presented when trying to select a bookmark, but none is found.
				_("No bookmarks found")
			)
			return
		if (
			isinstance(obj, chromium.ChromiumUIATreeInterceptor)
			or isinstance(obj, UIAHandler.browseMode.UIADocumentWithTableNavigation)
		):
			first = obj.makeTextInfo(textInfos.POSITION_FIRST)
			cur = obj.selection
			first.setEndPoint(cur, "endToStart")
			curPos = len(first.text)
		else:
			curPos = obj.makeTextInfo(textInfos.POSITION_CARET).bookmark.startOffset
		nextPos = None
		for pos in sorted(bookmarks):
			if pos > curPos:
				nextPos = pos
				break
		if nextPos is not None:
			moveToBookmark(nextPos)
			if not willSayAllResume(gesture):
				ui.message(
					# Translators: message presented when a bookmark is selected.
					_("Position: character %d") % nextPos
				)
			return
		ui.message(
			# Translators: message presented when the next bookmark is not found.
			_("Next bookmark not found")
		)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Moves to the previous bookmark."),
		resumeSayAllMode=sayAll.CURSOR.CARET,
		gesture="kb:NVDA+shift+y"
	)
	def script_selectPreviousBookmark(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		bookmarks = getSavedBookmarks()
		if bookmarks == {}:
			ui.message(
				# Translators: message presented when trying to select a bookmark, but none is found.
				_("No bookmarks found")
			)
			return
		if (
			isinstance(obj, chromium.ChromiumUIATreeInterceptor)
			or isinstance(obj, UIAHandler.browseMode.UIADocumentWithTableNavigation)
		):
			first = obj.makeTextInfo(textInfos.POSITION_FIRST)
			cur = obj.selection
			first.setEndPoint(cur, "endToStart")
			curPos = len(first.text)
		else:
			curPos = obj.makeTextInfo(textInfos.POSITION_CARET).bookmark.startOffset
		prevPos = None
		for pos in sorted(bookmarks, reverse=True):
			if pos < curPos:
				prevPos = pos
				break
		if prevPos is not None:
			moveToBookmark(prevPos)
			if not willSayAllResume(gesture):
				ui.message(
					# Translators: message presented when a bookmark is selected.
					_("Position: character %d") % prevPos
				)
			return
		ui.message(
			# Translators: message presented when the previous bookmark is not found.
			_("Previous bookmark not found")
		)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Shows the name of the current file for place markers in browse mode.")
	)
	def script_showCurrentBookmarksFile(self, gesture):
		obj = api.getFocusObject()
		if controlTypes.State.MULTILINE not in obj.states:
			treeInterceptor = obj.treeInterceptor
			if not(
				isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough
			):
				gesture.send()
				return
		message = getFile("bookmarks")
		if os.path.isfile(getFileBookmarks()):
			# Translators: Presented when the current document has positional bookmarks.
			message += "\r\n\r\n" + _("Has bookmarks.")
		if os.path.isfile(getFileSearch()):
			# Translators: Presented when the current document has specific search.
			message += "\r\n\r\n" + _("Has text for specific search.")
		if os.path.isfile(getFileTempBookmark()):
			# Translators: Presented when the current document has a temporary bookmark.
			message += "\r\n\r\n" + _("Has temporary bookmark.")
		ui.browseableMessage(
			# Translators: Title for a message presented when the file name for place markers is shown in browse mode.
			message, _("%s file") % ADDON_SUMMARY
		)

	@script(
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
		description=_("Saves the current position as a temporary bookmark.")
	)
	def script_saveTempBookmark(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		if isinstance(obj, chromium.ChromiumUIATreeInterceptor):
			first = obj.makeTextInfo(textInfos.POSITION_FIRST)
			cur = obj.selection
			first.setEndPoint(cur, "endToStart")
			startOffset = len(first.text)
		else:
			bookmark = obj.makeTextInfo(textInfos.POSITION_CARET).bookmark
			startOffset = bookmark.startOffset
		fileName = getFileTempBookmark()
		try:
			with open(fileName, "w", encoding="utf-8") as f:
				f.write(str(startOffset))
				# Translators: Message presented when a temporary bookmark is saved.
				ui.message(_("Saved temporary bookmark at position %d" % startOffset))
		except Exception as e:
			log.debugWarning("Error saving temporary bookmark", exc_info=True)
			raise e

	@script(
		# Translators: Message presented in input help mode.
		description=_("Moves to the temporary bookmark for the current document."),
		resumeSayAllMode=sayAll.CURSOR.CARET,
	)
	def script_moveToTempBookmark(self, gesture):
		obj = api.getFocusObject()
		appName = appModuleHandler.getAppNameFromProcessID(obj.processID, True)
		if appName == "MicrosoftEdgeCP.exe":
			gesture.send()
			return
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		else:
			gesture.send()
			return
		fileName = getFileTempBookmark()
		try:
			with open(fileName, "r", encoding="utf-8") as f:
				tempBookmark = int(f.read())
			moveToBookmark(tempBookmark)
		except Exception:
			# Translators: Message presented when a temporary bookmark can't be found.
			ui.message("Temporary bookmark not found")
