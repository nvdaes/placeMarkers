# -*- coding: UTF-8 -*-

# PlaceMarkers
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
import wx
import ui
import speech
import cPickle
import codecs
from cursorManager import CursorManager
from logHandler import log
from gui.settingsDialogs import SettingsDialog

addonHandler.initTranslation()

_basePath = unicode(os.path.join(os.path.dirname(__file__), "placeMarkers"))
_searchFolder = os.path.join(_basePath, "search")
searchFile = ""
lastSpecificFindText = ""
savedStrings = []
_bookmarksFolder = os.path.join(_basePath, "bookmarks")
_configPath = globalVars.appArgs.configPath


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

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
		self.aboutItem = self.BSMenu.Append(wx.ID_ANY,
		# Translators: the name for an item of addon submenu.
		_("Open &documentation"),
		# Translators: the tooltip text for an item of addon submenu.
		_("Open documentation for current language"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onAbout, self.aboutItem)

		self._pickle = ""
		self._states = []

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def createSearchFolder(self):
		if os.path.isdir(_searchFolder):
			return
		try:
			os.makedirs(_searchFolder)
		except Exception, e:
			log.debugWarning("Error creating search folder", exc_info=True)
			raise e

	def createBookmarksFolder(self):
		if os.path.isdir(_bookmarksFolder):
			return
		try:
			os.makedirs(_bookmarksFolder)
		except Exception, e:
			log.debugWarning("Error creating bookmarks folder", exc_info=True)
			raise e

	def onSpecificSearch(self, evt):
		self.createSearchFolder()
		try:
			os.startfile(_searchFolder)
		except WindowsError:
			pass

	def onBookmarks(self, evt):
		self.createBookmarksFolder()
		try:
			os.startfile(_bookmarksFolder)
		except WindowsError:
			pass

	def onCopy(self, evt):
		if not os.path.isdir(_basePath):
			return
		config.initConfigPath()
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: label of a dialog presented for copying place markers.
		_("Select a folder for copying your saved place markers"),
		_configPath, wx.DD_DEFAULT_STYLE)
		gui.mainFrame.prePopup()
		result = dlg.ShowModal()
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			copyPath = os.path.join(dlg.GetPath(), "placeMarkersBackup")
			try:
				shutil.rmtree(copyPath, ignore_errors=True)
				shutil.copytree(_basePath, copyPath)
			except Exception, e:
				wx.CallAfter(gui.messageBox,
				# Translators: label of error dialog shown when cannot copy placeMarkers folder.
				_("Folder not copied"),
				# Translators: title of error dialog shown when cannot copy placeMarkers folder.
				_("Copy Error"),
				wx.OK|wx.ICON_ERROR)
				raise e

	def onRestore(self, evt):
		placeMarkersPath = os.path.join(_configPath, "placeMarkersBackup")
		dlg = wx.DirDialog(gui.mainFrame,
		# Translators: label of a dialog presented for restoring place markers.
		_("Select the place markers folder you wish to restore"),
		placeMarkersPath, wx.DD_DIR_MUST_EXIST | wx.DD_DEFAULT_STYLE)
		gui.mainFrame.prePopup()
		result = dlg.ShowModal()
		gui.mainFrame.postPopup()
		if result == wx.ID_OK:
			placeMarkersPath = dlg.GetPath()
			try:
				shutil.rmtree(_basePath, ignore_errors=True)
				shutil.copytree(placeMarkersPath, _basePath)
			except Exception, e:
				wx.CallAfter(gui.messageBox,
				# Translators: label of error dialog shown when cannot copy placeMarkers folder.
				_("Folder not copied"),
				# Translators: title of error dialog shown when cannot copy placeMarkers folder.
				_("Copy Error"),
				wx.OK|wx.ICON_ERROR)
				raise e

	def getDocFolder(self):
		langs = [languageHandler.getLanguage(), "en"]
		for lang in langs:
			docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", lang)
			if os.path.isdir(docFolder):
				return docFolder
			if "_" in lang:
				tryLang = lang.split("_")[0]
				docFolder = os.path.join(os.path.dirname(__file__), "..", "doc", tryLang)
				if os.path.isdir(docFolder):
					return docFolder
				if tryLang == "en":
					break
			if lang == "en":
				break
		return None

	def getDocPath(self, docFileName):
		docPath = self.getDocFolder()
		if docPath is not None:
			docFile = os.path.join(docPath, docFileName)
			if os.path.isfile(docFile):
				docPath = docFile
		return docPath

	def onAbout(self, evt):
		try:
			os.startfile(self.getDocPath("readme.html"))
		except WindowsError:
			pass

	def standarFileName(self, fileName):
		fileName.encode("mbcs")
		notAllowed = re.compile("\?|:|\*|\t|<|>|\"|\/|\\||") # Invalid characters
		allowed = re.sub(notAllowed, "", unicode(fileName))
		return allowed

	def getFile(self, folder, ext=""):
		obj=api.getForegroundObject()
		file = obj.name
		obj = api.getFocusObject()
		try:
			obj = obj.treeInterceptor.rootNVDAObject
			childID = obj.IAccessibleChildID
			IAObj = obj.IAccessibleObject
			accValue = IAObj.accValue(childID)
			nameToAdd = " - %s" % accValue.split("/")[-1].split("\\")[-1]
		except:
			nameToAdd = ""
		file = file.rsplit(" - ", 1)[0]
		file = file.split("\\")[-1]
		file += nameToAdd
		file = self.standarFileName(file)
		folderPath = os.path.join(_basePath, folder)
		maxLenFileName = 232-len(folderPath)
		if maxLenFileName <= 0:
			return ""
		file = file[:maxLenFileName]
		file = file+ext
		path = os.path.join(folderPath, file)
		return path

	def getFileSearch(self):
		global searchFile
		searchFile = self.getFile("search", ".txt")

	def getSavedTexts(self):
		self.getFileSearch()
		global savedStrings
		try:
			with codecs.open(searchFile, "r", "utf-8") as f:
				savedStrings = f.read().split("\n")
		except Exception, e:
			savedStrings = []
			raise e

	def getLastSpecificFindText(self):
		self.getSavedTexts()
		global lastSpecificFindText
		try:
			lastSpecificFindText = savedStrings[0]
		except:
			pass

	def saveSpecificFindTextDialog(self):
		try:
			self.getLastSpecificFindText()
		except:
			global lastSpecificFindText
			lastSpecificFindText = ""
		d = wx.TextEntryDialog(gui.mainFrame,
		# Translators: label of a dialog presented to save or delete a string for specific search.
		_("Type the text you wish to save, or delete any text if you want to remove it from the previous saved searches"),
		# Translators: title of a dialog presented to save a string for specific search.
		_("Save text for specific search"),
		defaultValue=lastSpecificFindText)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.saveSpecificFindText, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def saveSpecificFindText(self, text):
		self.createSearchFolder()
		if not text:
			try:
				os.remove(searchFile)
			except WindowsError:
				log.debugWarning("Error deleting specific search file", exc_info=True)
			return
		if "\n" in text:
			return
		if text in savedStrings:
			return
		savedStrings.insert(0, text)
		textToSave = "\n".join(savedStrings)
		try:
			with codecs.open(searchFile, "w", "utf-8") as f:
				f.write(textToSave)
		except Exception, e:
			log.debugWarning("Error saving specific search", exc_info=True)
			raise e

	def script_specificSave(self,gesture):
		obj=api.getFocusObject()
		if not controlTypes.STATE_MULTILINE in obj.states:
			treeInterceptor=obj.treeInterceptor
			if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough):
				return
		self.saveSpecificFindTextDialog()
		# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_specificSave.__doc__ = _("Saves a text string for a specific search.")

	def doFindText(self,text,reverse=False):
		if not text:
			return
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
			CursorManager._lastFindText=text
		elif not controlTypes.STATE_MULTILINE in obj.states:
			return
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			info=obj.makeTextInfo(textInfos.POSITION_FIRST)
		try:
			res=info.find(text,reverse=reverse)
		except WindowsError:
			wx.CallAfter(gui.messageBox,
			# Translators: label of error dialog.
			_('text "%s" not found')%text,
			# Translators: title of error dialog.
			_("Find Error"),
			wx.OK|wx.ICON_ERROR)
		except:
			if api.copyToClip(text):
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
			# Translators: label of error dialog.
			_('text "%s" not found')%text,
			# Translators: title of error dialog.
			_("Find Error"),
			wx.OK|wx.ICON_ERROR)

	def doFindTextUp(self, text):
		self.doFindText(text, reverse=True)

	def script_specificFind(self,gesture):
		obj=api.getFocusObject()
		if not controlTypes.STATE_MULTILINE in obj.states:
			treeInterceptor=obj.treeInterceptor
			if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough):
				return
		try:
			self.getLastSpecificFindText()
		except:
			ui.message(
			# Translators: message presented when there is not file for specific search.
			_("File for specific search not found"))
			return
		GMF = gui.MainFrame()
		GMF._popupSettingsDialog(SpecificSearchDialog)
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
		self.createBookmarksFolder()
		self._pickle = self.getFile("bookmarks", ".pickle")

	def script_saveBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
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
		except Exception, e:
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
				end.move(textInfos.UNIT_LINE,1,endPoint="end")
				speech.speakTextInfo(end,reason=controlTypes.REASON_CARET)
				ui.message(
				# Translators: message presented when a bookmark is selected.
				_("Position: character %d") % bookmark)
				return
		ui.message(
		# Translators: message presented when the next bookmark is not found.
		_("Next bookmark not found"))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_selectNextBookmark.__doc__ = _("Moves to the next bookmark.")

	def script_selectPreviousBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
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
				end.move(textInfos.UNIT_LINE,1,endPoint="end")
				speech.speakTextInfo(end,reason=controlTypes.REASON_CARET)
				ui.message(
				# Translators: message presented when a bookmark is selected.
				_("Position: character %d") % bookmark)
				return
		ui.message(
		# Translators: message presented when the previous bookmark is not found.
		_("Previous bookmark not found"))
	# Translators: message presented in input mode, when a keystroke of an addon script is pressed.
	script_selectPreviousBookmark.__doc__ = _("Moves to the previous bookmark.")

	def script_copyCurrentBookmarksFile(self, gesture):
		obj=api.getFocusObject()
		if not controlTypes.STATE_MULTILINE in obj.states:
			treeInterceptor=obj.treeInterceptor
			if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough) and controlTypes.STATE_MULTILINE not in obj.states:
				return
		fileName = self.getFile("bookmarks")
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
		"kb:control+shift+NVDA+s": "specificSave",
		"kb:control+shift+NVDA+f": "specificFind",
		"kb:control+shift+NVDA+k": "saveBookmark",
		"kb:control+shift+NVDA+delete": "deleteBookmark",
		"kb:control+shift+k": "selectNextBookmark",
		"kb:shift+NVDA+k": "selectPreviousBookmark",
		"kb:NVDA+k": "copyCurrentBookmarksFile",
	}

class SpecificSearchDialog(SettingsDialog):
	# Translators: This is the label for the specific search settings dialog.
	title = _("Specific Search")
	GP = GlobalPlugin()

	def makeSettings(self, settingsSizer):
		# Translators: This is the label for a textfield in the
		# specific search settings dialog.
		textToSearchLabel=wx.StaticText(self,-1,label=_("&Text to search:"))
		settingsSizer.Add(textToSearchLabel)
		self.textToSearchEdit=wx.TextCtrl(self,wx.NewId())
		self.textToSearchEdit.SetValue(lastSpecificFindText)
		settingsSizer.Add(self.textToSearchEdit,border=10,flag=wx.BOTTOM)

		textsListSizer=wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in specific search to select a saved text.
		textsListLabel=wx.StaticText(self,-1,label=_("&Saved texts:"))
		textsListSizer.Add(textsListLabel)
		textsListID=wx.NewId()
		# Translators: A combo box to choose a saved text.
		self.textsList=wx.Choice(self,textsListID, name=_("Saved texts to search:"), choices=[name for name in savedStrings])
		self.textsList.SetSelection(0)
		textsListSizer.Add(self.textsList)
		settingsSizer.Add(textsListSizer,border=10,flag=wx.BOTTOM)

		actionsListSizer=wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the name of an action presented in specific search dialog.
		searchDownAction = _("Search down")
		# Translators: the name of an action presented in specific search dialog.
		searchUpAction = _("Search up")
		# Translators: the name of an action presented in specific search dialog.
		deleteAction = _("Delete")
		actions = [searchDownAction, searchUpAction, deleteAction]
		# Translators: The label for a setting in specific search to select an action.
		actionsListLabel=wx.StaticText(self,-1,label=_("&Actions to choose:"))
		actionsListSizer.Add(actionsListLabel)
		actionsListID=wx.NewId()
		# Translators: A combo box to choose an action.
		self.actionsList=wx.Choice(self,actionsListID, name=_("Select an action to perform:"), choices=[name for name in actions])
		self.actionsList.SetSelection(0)
		actionsListSizer.Add(self.actionsList)
		settingsSizer.Add(actionsListSizer,border=10,flag=wx.BOTTOM)

		self.textsList.Bind(wx.EVT_CHOICE, self.onChoice)

	def postInit(self):
		self.textToSearchEdit.SetFocus()

	def onChoice(self, evt):
		self.textToSearchEdit.SetValue(self.textsList.GetStringSelection())

	def onOk(self,evt):
		textToSearch = self.textToSearchEdit.GetValue()
		actionToPerform = self.actionsList.GetSelection()
		if actionToPerform == 0:
			wx.CallLater(100, self.GP.doFindText, textToSearch)
		elif actionToPerform == 1:
			wx.CallLater(100, self.GP.doFindTextUp, textToSearch)
		else:
			global savedStrings
			try:
				savedStrings.pop(self.textsList.GetSelection())
			except Exception, e:
				log.debugWarning("Error removing item from savedStrings", exc_info=True)
				raise e
			if len(savedStrings) < 1:
				try:
					os.unlink(searchFile)
				except Exception, e:
					log.debugWarning("Error removing specific search file", exc_info=True)
					raise e
			else:
				textToSave = "\n".join(savedStrings)
				try:
					with codecs.open(searchFile, "w", "utf-8") as f:
						f.write(textToSave)
				except Exception, e:
					log.debugWarning("Error saving strings of text for specific search", exc_info=True)
					raise e
		super(SpecificSearchDialog, self).onOk(evt)

