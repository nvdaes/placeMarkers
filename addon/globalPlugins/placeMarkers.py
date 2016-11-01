# -*- coding: UTF-8 -*-
# placeMarkers: Plugin to manage place markers based on positions or strings in specific documents
#Copyright (C) 2012-2016 Noelia Ruiz Martínez
# Released under GPL 2

# Gestures sent to applications when add-on features are not applicable
# Date: 1/09/2015
# Changed key commands
# Date: 27/02/2015
# Removed Open documentation option from add-on menu, as suggested by Bernd Dorer
# Date: 16/02/2015
# Added case sensitive search
# Date: 2/02/2015
# Removed fragment identifiers in bookmark filenames
# Date: 24/06/2014
# Support for enhanced skim reading in version 2014.1.
# Date: 13/03/2014
# Support for skim reading.
# Date: 28/10/2013
# Assigned script categories for input gestures
# Date: 12/10/2013
# PlaceMarkers
# Used decode("mbcs") instead of unicode in _basePath variable
# Date: 21/09/2013
# Added searched strings history
# Date: 01/07/2013
# Limited length of file names
# Date: 04/05/2013
# Added support for cyrillic characters
# Date: 1/05/2013
# Create placeMarkers folders if don't exist
# Date: 25/04/2013
# Added a different keystroke to delete bookmarks
# Date: 16/04/2013
# Version: 2.0: Added accValue in file names to use EPUBReader
# Date: 31/03/2013
# Version: 1.1
# Date: 03/08/2012

import addonHandler
import globalPluginHandler
import api
import re
import os
import shutil
import config
import globalVars
import languageHandler
import textInfos
import controlTypes
import gui
from gui import guiHelper
import wx
import ui
import speech
import cPickle
import codecs
import sayAllHandler
from scriptHandler import willSayAllResume
from cursorManager import CursorManager
from logHandler import log

addonHandler.initTranslation()

_addonDir = os.path.join(os.path.dirname(__file__), "..") # The root of an addon folder
_curAddon = addonHandler.Addon(_addonDir) # Addon instance
_addonSummary = _curAddon.manifest['summary']
_basePath = os.path.join(os.path.dirname(__file__), "placeMarkers").decode("mbcs")
_searchFolder = os.path.join(_basePath, "search")
_bookmarksFolder = os.path.join(_basePath, "bookmarks")
_configPath = globalVars.appArgs.configPath

def createSearchFolder():
	if os.path.isdir(_searchFolder):
		return
	try:
		os.makedirs(_searchFolder)
	except Exception as e:
		log.debugWarning("Error creating search folder", exc_info=True)
		raise e

def createBookmarksFolder():
	if os.path.isdir(_bookmarksFolder):
		return
	try:
		os.makedirs(_bookmarksFolder)
	except Exception as e:
		log.debugWarning("Error creating bookmarks folder", exc_info=True)
		raise e

createSearchFolder()
createBookmarksFolder()

def doFindText(text, reverse=False, caseSensitive=False):
	if not text:
		return
	obj=api.getFocusObject()
	treeInterceptor=obj.treeInterceptor
	if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
		obj=treeInterceptor
		CursorManager._lastFindText=text
		CursorManager._lastCaseSensitivity=caseSensitive
	elif obj.role != controlTypes.ROLE_EDITABLETEXT:
		return
	try:
		info=obj.makeTextInfo(textInfos.POSITION_CARET)
	except (NotImplementedError, RuntimeError):
		info=obj.makeTextInfo(textInfos.POSITION_FIRST)
	try:
		res=info.find(text,reverse=reverse, caseSensitive=caseSensitive)
	except WindowsError:
		wx.CallAfter(gui.messageBox,
	# Translators: label of error dialog, translated in NVDA core.
		_('text "%s" not found')%text,
		# Translators: title of error dialog, translated in NVDA core.
		_("Find Error"),
		wx.OK|wx.ICON_ERROR)
	except:
		if api.copyToClip(text):
			# Translators: message presented when a string of text has been copied to the clipboard.
			ui.message(_("%s copied to clipboard") % text)
		return
	if res:
		if hasattr(obj,'selection'):
			obj.selection=info
		else:
			info.updateCaret()
		speech.cancelSpeech()
		info.move(textInfos.UNIT_LINE,1,endPoint="end")
		speech.speakTextInfo(info,reason=controlTypes.REASON_CARET)
	else:
		wx.CallAfter(gui.messageBox,
		# Translators: label of error dialog, translated in NVDA core.
		_('text "%s" not found')%text,
		# Translators: title of error dialog, translated in NVDA core.
		_("Find Error"),
		wx.OK|wx.ICON_ERROR)

def doFindTextUp(text, caseSensitive=False):
	doFindText(text, reverse=True, caseSensitive=caseSensitive)

def standarFileName(fileName):
	fileName.encode("mbcs")
	notAllowed = re.compile("\?|:|\*|\t|<|>|\"|\/|\\||") # Invalid characters
	allowed = re.sub(notAllowed, "", unicode(fileName))
	return allowed

def getFile(folder, ext=""):
	obj=api.getForegroundObject()
	file = obj.name
	obj = api.getFocusObject()
	try:
		obj = obj.treeInterceptor.rootNVDAObject
		childID = obj.IAccessibleChildID
		iAObj = obj.IAccessibleObject
		accValue = iAObj.accValue(childID)
		nameToAdd = " - %s" % accValue.split("/")[-1].split("\\")[-1].split("#")[0]
	except:
		nameToAdd = ""
	file = file.rsplit(" - ", 1)[0]
	file = file.split("\\")[-1]
	file += nameToAdd
	file = standarFileName(file)
	folderPath = os.path.join(_basePath, folder)
	maxLenFileName = 232-len(folderPath)
	if maxLenFileName <= 0:
		return ""
	file = file[:maxLenFileName]
	file = file+ext
	path = os.path.join(folderPath, file)
	return path

def getFileSearch():
	return getFile("search", ".txt")

def getSavedTexts():
	searchFile = getFileSearch()
	try:
		with codecs.open(searchFile, "r", "utf-8") as f:
			savedStrings = f.read().split("\n")
	except:
		savedStrings = []
	return savedStrings

def getLastSpecificFindText():
	try:
		return getSavedTexts()[0]
	except:
		return ""

class SpecificSearchDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of the Specific Search dialog.
		super(SpecificSearchDialog, self).__init__(parent, title=_("Specific search"))
		self.searchFile = getFileSearch()
		self.savedTexts = getSavedTexts()
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Translators: The label of a combo box in the Specific Search dialog.
		savedTextsLabel = _("&Saved texts")
		self.savedTextsComboBox = sHelper.addLabeledControl(savedTextsLabel, wx.Choice, choices=self.savedTexts)
		self.savedTextsComboBox.Bind(wx.EVT_CHOICE, self.onSavedTextsChange)
		# Translators: A label for a chekbox in the Specific search dialog.
		self.removeCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Remove from history")))
		self.removeCheckBox.Disable()
		# Translators: The label of an edit box in the Specific Search dialog.
		searchTextLabel = _("&Text to search:")
		searchLabeledCtrl = gui.guiHelper.LabeledControlHelper(self, searchTextLabel, wx.TextCtrl)
		self.searchTextEdit = searchLabeledCtrl.control
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
		self.searchRadioBox=sHelper.addItem(wx.RadioBox(self,label=searchActionsLabel, choices=searchChoices))
		self.searchRadioBox.Bind(wx.EVT_RADIOBOX, self.onSearchRadioBox)
		# Translators: A label for a chekbox in the Specific search dialog.
		self.caseSensitiveCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Case-sensitive search")))
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.searchTextEdit.SetFocus()
		if not self.searchTextEdit.Value:
			self.addCheckBox.Disable()
			self.searchRadioBox.Disable()
			self.caseSensitiveCheckBox.Disable()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

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
		if self.searchRadioBox.Selection == 2: # Don't search
			self.caseSensitiveCheckBox.Disable()

	def onOk(self, evt):
		self.Destroy()
		if self.addCheckBox.Value or self.searchRadioBox.Selection < 2: # Add or search
			text = self.searchTextEdit.Value
		actionToPerform = self.searchRadioBox.Selection
		if actionToPerform < 2: # Search
			caseSensitive = self.caseSensitiveCheckBox.Value
			if actionToPerform == 0:
				wx.CallLater(100, doFindText, text, caseSensitive=caseSensitive)
			else:
				wx.CallLater(100, doFindTextUp, text, caseSensitive=caseSensitive)
		if self.addCheckBox.Value or self.removeCheckBox.Value:
			savedStrings = self.savedTexts
			if self.removeCheckBox.Value:
				del savedStrings[self.savedTextsComboBox.Selection]
			if self.addCheckBox.Value and not "\n" in text and not text in savedStrings:
				savedStrings.insert(0, text)
			if len(savedStrings) == 0:
				os.remove(self.searchFile)
				return
			try:
				with codecs.open(self.searchFile, "w", "utf-8") as f:
					f.write("\n".join(savedStrings))
			except Exception as e:
				log.debugWarning("Error saving strings of text for specific search", exc_info=True)
				raise e

def doCopy(copyDirectory):
	try:
		shutil.rmtree(copyDirectory, ignore_errors=True)
		shutil.copytree(_basePath, copyDirectory)
	except Exception as e:
		wx.CallAfter(gui.messageBox,
		# Translators: label of error dialog shown when cannot copy placeMarkers folder.
		_("Folder not copied"),
		# Translators: title of error dialog shown when cannot copy placeMarkers folder.
		_("Copy Error"),
		wx.OK|wx.ICON_ERROR)
		raise e

def doRestore(restoreDirectory):
	try:
		shutil.rmtree(_basePath, ignore_errors=True)
		shutil.copytree(restoreDirectory, _basePath)
	except Exception as e:
		wx.CallAfter(gui.messageBox,
		# Translators: label of error dialog shown when cannot copy placeMarkers folder.
		_("Folder not copied"),
		# Translators: title of error dialog shown when cannot copy placeMarkers folder.
		_("Copy Error"),
		wx.OK|wx.ICON_ERROR)
		raise e

class CopyDialog(wx.Dialog):

	_instance = None
	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		if CopyDialog._instance is None:
			return super(CopyDialog, cls).__new__(cls, *args, **kwargs)
		return CopyDialog._instance

	def __init__(self, parent):
		if CopyDialog._instance is not None:
			return
		CopyDialog._instance = self
		# Translators: The title of the Copy dialog.
		super(CopyDialog, self).__init__(parent, title=_("Copy place markers"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Copy dialog.
		dialogCaption=_("""Select a folder to save a backup of your current place markers.\n
		They will be copied from %s.""" % _basePath)
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory in the Copy dialog.
		directoryGroupText = _("directory for backup:")
		groupHelper = sHelper.addItem(gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)))
		# Translators: The label of a button to browse for a directory.
		browseText = _("Browse...")
		# Translators: The title of the dialog presented when browsing for the destination directory when copying place markers.
		dirDialogTitle = _("Select directory to copy")
		directoryEntryControl = groupHelper.addItem(gui.guiHelper.PathSelectionHelper(self, browseText, dirDialogTitle))
		self.copyDirectoryEdit = directoryEntryControl.pathControl
		self.copyDirectoryEdit.Value = os.path.join(_configPath, "placeMarkersBackup")
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		continueButton = bHelper.addButton(self, label=_("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onCopy)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onCopy(self, evt):
		if not self.copyDirectoryEdit.Value:
			# Translators: The message displayed when the user has not specified a destination directory in the Copy dialog.
			gui.messageBox(_("Please specify a directory."),
				_("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		drv=os.path.splitdrive(self.copyDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Translators: The message displayed when the user specifies an invalid destination drive, translated in NVDA core.
			gui.messageBox(_("Invalid drive %s")%drv,
				_("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		self.Hide()
		doCopy(self.copyDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

class RestoreDialog(wx.Dialog):

	_instance = None
	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		if RestoreDialog._instance is None:
			return super(RestoreDialog, cls).__new__(cls, *args, **kwargs)
		return RestoreDialog._instance

	def __init__(self, parent):
		if RestoreDialog._instance is not None:
			return
		RestoreDialog._instance = self
		# Translators: The title of the Restore dialog.
		super(RestoreDialog, self).__init__(parent, title=_("Restore place markers"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: An informational message displayed in the Restore dialog.
		dialogCaption=_("""Select a folder to restore a backup of your previous copied place markers.\n
		They will be copied to %s.""" % _basePath)
		sHelper.addItem(wx.StaticText(self, label=dialogCaption))

		# Translators: The label of a grouping containing controls to select the destination directory in the Restore dialog.
		directoryGroupText = _("directory containing backup:")
		groupHelper = sHelper.addItem(gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=directoryGroupText), wx.VERTICAL)))
		# Translators: The label of a button to browse for a directory.
		browseText = _("Browse...")
		# Translators: The title of the dialog presented when browsing for the destination directory when restoring place markers.
		dirDialogTitle = _("Select directory to restore")
		directoryEntryControl = groupHelper.addItem(gui.guiHelper.PathSelectionHelper(self, browseText, dirDialogTitle))
		self.restoreDirectoryEdit = directoryEntryControl.pathControl
		self.restoreDirectoryEdit.Value = os.path.join(_configPath, "placeMarkersBackup")
		bHelper = sHelper.addDialogDismissButtons(gui.guiHelper.ButtonHelper(wx.HORIZONTAL))
		continueButton = bHelper.addButton(self, label=_("&Continue"), id=wx.ID_OK)
		continueButton.SetDefault()
		continueButton.Bind(wx.EVT_BUTTON, self.onRestore)
		bHelper.addButton(self, id=wx.ID_CANCEL)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		self.Sizer = mainSizer
		mainSizer.Fit(self)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onRestore(self, evt):
		if not self.restoreDirectoryEdit.Value:
			# Translators: The message displayed when the user has not specified a destination directory in the Restore dialog.
			gui.messageBox(_("Please specify a directory."),
				_("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		drv=os.path.splitdrive(self.restoreDirectoryEdit.Value)[0]
		if drv and not os.path.isdir(drv):
			# Translators: The message displayed when the user specifies an invalid destination drive, translated in NVDA core.
			gui.messageBox(_("Invalid drive %s")%drv,
				_("Error"),
				wx.OK | wx.ICON_ERROR)
			return
		self.Hide()
		doRestore(self.restoreDirectoryEdit.Value)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = unicode(_addonSummary)

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		#self.menu = gui.mainFrame.sysTrayIcon.menu
		self.BSMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.BSMenu,
		# Translators: the name of addon submenu.
		_("P&lace markers"),
		# Translators: the tooltip text for addon submenu.
		_("Bookmarks and Search menu"))
		self.searchItem = self.BSMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Specific search folder"),
		# Translators: the tooltip text for an item of addon submenu.
		_("Opens the specific search folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSpecificSearch, self.searchItem)
		self.bookmarksItem = self.BSMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Bookmarks folder"),
		# Translators: the tooltip text for an item of addon submenu.
		_("Opens the bookmarks folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onBookmarks, self.bookmarksItem)
		self.copyItem = self.BSMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("&Copy placeMarkers folder..."),
		# Translators: the tooltip text for an item of addon submenu.
		_("Backup of place markers"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onCopy, self.copyItem)
		self.restoreItem = self.BSMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("R&estore place markers..."),
		# Translators: the tooltip text for an item of addon submenu.
		_("Restore previously saved place markers"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onRestore, self.restoreItem)
		self._pickle = ""
		self._states = []

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onSpecificSearch(self, evt):
		try:
			os.startfile(_searchFolder)
		except WindowsError:
			pass

	def onBookmarks(self, evt):
		try:
			os.startfile(_bookmarksFolder)
		except WindowsError:
			pass

	def onCopy(self, evt):
		gui.mainFrame.prePopup()
		d = CopyDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def onRestore(self, evt):
		gui.mainFrame.prePopup()
		d = RestoreDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def popupSpecificSearchDialog(self):
		if gui.isInMessageBox:
			return
		gui.mainFrame.prePopup()
		d = SpecificSearchDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

	def script_specificFind(self,gesture):
		obj=api.getFocusObject()
		if not controlTypes.STATE_MULTILINE in obj.states:
			treeInterceptor=obj.treeInterceptor
			if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough):
				gesture.send()
				return
		wx.CallAfter(self.popupSpecificSearchDialog)
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_specificFind.__doc__ = _("finds a text string from the current cursor position for a specific document.")

	def getStates(self):
		self.getPickle()
		fileName = self._pickle
		try:
			self._states = cPickle.load(file(fileName, "r"))
		except IOError:
			self._states = []

	def getPickle(self):
		self._pickle = getFile("bookmarks", ".pickle")

	def script_saveBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
			gesture.send()
			return
		self.getStates()
		fileName = self._pickle
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(
			# Translators: message presented when a bookmark cannot be saved.
			_("Bookmark cannot be saved"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		if count in self._states:
			ui.message(
			# Translators: message presented when the current position was previously saved as a bookmark.
			_("This position was already saved"))
			return
		self._states.append(count)
		self._states.sort()
		try:
			cPickle.dump(self._states, file(fileName, "wb"))
			ui.message(
			# Translators: message presented when a position is saved as a bookmark.
			_("Saved position at character %d") %count)
		except Exception as e:
			log.debugWarning("Error saving bookmark", exc_info=True)
			ui.message(
			# Translators: message presented when a bookmark cannot be saved.
			_("Cannot save bookmark"))
			raise e
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_saveBookmark.__doc__ = _("Saves the current position as a bookmark.")

	def script_deleteBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
			gesture.send()
			return
		self.getStates()
		if len(self._states) == 0:
			ui.message(
			# Translators: message presented when the current document doesn't contain bookmarks.
			_("No bookmarks"))
			return
		fileName = self._pickle
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(_("Bookmark cannot be deleted"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		if count not in self._states:
			ui.message(
			# Translators: message presented when the current document has bookmarks, but none is selected.
			_("No bookmark selected"))
			return
		self._states.remove(count)
		if len(self._states) > 0:
			self._states.sort()
			try:
				cPickle.dump(self._states, file(fileName, "wb"))
				ui.message(
				# Translators: message presented when a bookmark is deleted.
				_("Bookmark deleted"))
				return
			except:
				pass
		else:
			try:
				os.remove(fileName)
				ui.message(_
				# Translators: message presented when the current document doesn't contain bookmarks.
				("No bookmarks"))
				return
			except WindowsError:
				pass
		log.debugWarning("Error saving bookmarks", exc_info=True)
		ui.message(
		# Translators: message presented when cannot delete a bookmark.
		_("Cannot delete bookmark"))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_deleteBookmark.__doc__ = _("Deletes the current bookmark.")

	def script_selectNextBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
			gesture.send()
			return
		self.getStates()
		if len(self._states) == 0:
			ui.message(
			# Translators: message presented when trying to select a bookmark, but none is found.
			_("No bookmarks found"))
			return
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(
			# Translators: message presented when cannot find any bookmark.
			_("Cannot find any bookmark"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		for bookmark in self._states:
			if bookmark > count:
				end.move(textInfos.UNIT_CHARACTER, bookmark-count)
				obj.selection = end
				if not willSayAllResume(gesture):
					end.move(textInfos.UNIT_LINE,1,endPoint="end")
					speech.speakTextInfo(end,reason=controlTypes.REASON_CARET)
					ui.message(
					# Translators: message presented when a bookmark is selected.
					_("Position: character %d") % bookmark)
				return
		ui.message(
		# Translators: message presented when the next bookmark is not found.
		_("Next bookmark not found"))
	script_selectNextBookmark.resumeSayAllMode=sayAllHandler.CURSOR_CARET
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_selectNextBookmark.__doc__ = _("Moves to the next bookmark.")

	def script_selectPreviousBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
			gesture.send()
			return
		self.getStates()
		if len(self._states) == 0:
			ui.message(
			# Translators: message presented when trying to select a bookmark, but none is found.
			_("No bookmarks found"))
			return
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
		# Translators: message presented when cannot find any bookmark.
			ui.message(_("Cannot find any bookmark"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		bookmarkList = self._states
		bookmarkList.reverse()
		for bookmark in bookmarkList:
			if bookmark < count:
				end.move(textInfos.UNIT_CHARACTER, bookmark-count)
				obj.selection = end
				if not willSayAllResume(gesture):
					end.move(textInfos.UNIT_LINE,1,endPoint="end")
					speech.speakTextInfo(end,reason=controlTypes.REASON_CARET)
					ui.message(
					# Translators: message presented when a bookmark is selected.
					_("Position: character %d") % bookmark)
				return
		ui.message(
		# Translators: message presented when the previous bookmark is not found.
		_("Previous bookmark not found"))
	script_selectPreviousBookmark.resumeSayAllMode=sayAllHandler.CURSOR_CARET
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_selectPreviousBookmark.__doc__ = _("Moves to the previous bookmark.")

	def script_copyCurrentBookmarksFile(self, gesture):
		obj=api.getFocusObject()
		if not controlTypes.STATE_MULTILINE in obj.states:
			treeInterceptor=obj.treeInterceptor
			if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough) and controlTypes.STATE_MULTILINE not in obj.states:
				gesture.send()
				return
		fileName = getFile("bookmarks")
		if not api.copyToClip(os.path.basename(fileName)):
			ui.message(
			# Translators: message presented when cannot copy the file name corresponding to place markers.
			_("Cannot copy file name for place markers"))
			return
		ui.message(
		# Translators: message presented when file name for place markers is copied to clipboard.
		_("Place markers file name copied to clipboard"))
			# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_copyCurrentBookmarksFile.__doc__ = _("Copies the name of the current file for place markers to the clipboard.")

	__gestures = {
		"kb:control+shift+NVDA+f": "specificFind",
		"kb:control+shift+NVDA+k": "saveBookmark",
		"kb:control+shift+NVDA+delete": "deleteBookmark",
		"kb:NVDA+k": "selectNextBookmark",
		"kb:shift+NVDA+k": "selectPreviousBookmark",
		"kb:control+shift+k": "copyCurrentBookmarksFile",
	}
