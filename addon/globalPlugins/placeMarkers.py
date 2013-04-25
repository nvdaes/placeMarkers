# -*- coding: UTF-8 -*-

# Bookmark&Search
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
import languageHandler
import textInfos
import controlTypes
import gui
import wx
import ui
import speech
import cPickle
from cursorManager import CursorManager
from logHandler import log

addonHandler.initTranslation()

_basePath = os.path.join(os.path.dirname(__file__), "placeMarkers")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		#self.menu = gui.mainFrame.sysTrayIcon.menu
		self.BSMenu = wx.Menu()
		self.mainItem = self.menu.AppendSubMenu(self.BSMenu, _("Place &markers"), _("Bookmarks and Search menu"))
		self.searchItem = self.BSMenu.Append(wx.ID_ANY, _("&Specific search folder"), _("Open specific search folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSpecificSearch, self.searchItem)
		self.bookmarksItem = self.BSMenu.Append(wx.ID_ANY, _("&Bookmarks folder"), _("Open bookmarks folder"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onBookmarks, self.bookmarksItem)
		self.aboutItem = self.BSMenu.Append(wx.ID_ANY, _("Open &documentation"), _("Open documentation for current language"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onAbout, self.aboutItem)

		self._lastSpecificFindText = ""
		self._pickle = ""
		self._states = []

	def terminate(self):
		try:
			self.menu.RemoveItem(self.mainItem)
		except wx.PyDeadObjectError:
			pass

	def onSpecificSearch(self, evt):
		searchFolder = os.path.join(_basePath, "search")
		try:
			os.startfile(searchFolder)
		except WindowsError:
			pass

	def onBookmarks(self, evt):
		bookmarksFolder = os.path.join(_basePath, "bookmarks")
		try:
			os.startfile(bookmarksFolder)
		except WindowsError:
			pass

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
		notAllowed = re.compile("\?|:|\*|\t|<|>|\"|\/|\\||") # Invalid characters
		allowed = re.sub(notAllowed, "", unicode(fileName))
		return allowed

	def getFile(self, folder, ext=""):
		obj=api.getForegroundObject()
		file = obj.name
		nameToAdd = ""
		obj = api.getFocusObject()
		obj = obj.treeInterceptor.rootNVDAObject
		childID = obj.IAccessibleChildID
		IAObj = obj.IAccessibleObject
		accValue = IAObj.accValue(childID)
		nameToAdd = " - %s" % accValue.split("/")[-1]
		file = file.rsplit(" - ", 1)[0]
		file = file.split("\\")[-1]
		file += nameToAdd
		file = self.standarFileName(file)
		file = file+ext
		path = os.path.join(_basePath, folder, file)
		return path

	def getFileSearch(self):
		return self.getFile("search", ".txt")

	def getLastSpecificFindText(self):
		f = open(self.getFileSearch(), "r")
		self._lastSpecificFindText = f.read()
		f.close()

	def saveSpecificFindTextDialog(self):
		try:
			self.getLastSpecificFindText()
		except IOError:
			self._lastSpecificFindText = ""
		d = wx.TextEntryDialog(gui.mainFrame, _("Type the text you wish to save, or delete text if you want to remove the previous saved search"), _("Save text for specific search"), defaultValue=self._lastSpecificFindText)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.saveSpecificFindText, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def saveSpecificFindText(self, text):
		if not text:
			try:
				os.remove(self.getFileSearch())
			except WindowsError:
				log.debugWarning("Error deleting specific search file", exc_info=True)

			return
		try:
			f = open (self.getFileSearch(), "w")
			f.write(text.encode("mbcs"))
			f.close
		except:
			log.debugWarning("Error saving specific search", exc_info=True)


	def script_specificSave(self,gesture): 
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough):
			return
		self.saveSpecificFindTextDialog()
	script_specificSave.__doc__ = _("Saves a text string for a specific search.")

	def doFindText(self,text,reverse=False):
		if not text:
			return
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			info=obj.makeTextInfo(textInfos.POSITION_FIRST)
		res=info.find(text,reverse=reverse)
		if res:
			obj.selection=info
			speech.cancelSpeech()
			info.move(textInfos.UNIT_LINE,1,endPoint="end")
			speech.speakTextInfo(info,reason=controlTypes.REASON_CARET)
		else:
			wx.CallAfter(gui.messageBox,_('text "%s" not found')%text,_("Find Error"),wx.OK|wx.ICON_ERROR)
		CursorManager._lastFindText=text

	def doSpecificFindTextDialog(self):
		try:
			self.getLastSpecificFindText()
		except IOError:
			ui.message(_("File for specific search not found"))
			return
		d = wx.TextEntryDialog(gui.mainFrame, _("Type the text you wish to find"), _("Specific search"), defaultValue=self._lastSpecificFindText)
		def callback(result):
			if result == wx.ID_OK:
				# Make sure this happens after focus returns to the document.
				wx.CallLater(100, self.doFindText, d.GetValue())
		gui.runScriptModalDialog(d, callback)

	def script_specificFind(self,gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if not (hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough):
			return
		self.doSpecificFindTextDialog()
	script_specificFind.__doc__ = _("finds a text string from the current cursor position for a specific document.")

	def getStates(self):
		self.getPickle()
		fileName = self._pickle
		try:
			self._states = cPickle.load(file(fileName, "r"))
		except IOError:
			self._states = []

	def getPickle(self):
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
			ui.message(_("Bookmark can not be saved"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		if count in self._states:
			ui.message(_("This position was already saved"))
			return
		self._states.append(count)
		self._states.sort()
		try:
			cPickle.dump(self._states, file(fileName, "wb"))
			ui.message(_("Saved position: character %d") %count)
		except:
			log.debugWarning("Error saving bookmark", exc_info=True)

			ui.message(_("Cannot save bookmark"))
	script_saveBookmark.__doc__ = _("Saves the current position as a bookmark. Pressed two times, deletes the bookmark corresponding to the current position.")

	def script_deleteBookmark(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if hasattr(treeInterceptor,'TextInfo') and not treeInterceptor.passThrough:
			obj=treeInterceptor
		else:
			return
		self.getStates()
		if len(self._states) == 0:
			ui.message(_("No bookmarks"))
			return
		fileName = self._pickle
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(_("Bookmark can not be deleted"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		if count not in self._states:
			ui.message(_("No bookmark selected"))
			return
		self._states.remove(count)
		if len(self._states) > 0:
			self._states.sort()
			try:
				cPickle.dump(self._states, file(fileName, "wb"))
				ui.message(_("Bookmark deleted"))
				return
			except:
				pass
		else:
			try:
				os.remove(fileName)
				ui.message(_("No bookmarks"))
				return
			except WindowsError:
				pass
		log.debugWarning("Error saving bookmarks", exc_info=True)

		ui.message(_("Cannot delete bookmark"))
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
			ui.message(_("No bookmarks found"))
			return
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(_("Can not find bookmark"))
			return
		start.setEndPoint(end, "endToStart")
		count = len(start.text)
		for bookmark in self._states:
			if bookmark > count:
				end.move(textInfos.UNIT_CHARACTER, bookmark-count)
				obj.selection = end
				end.move(textInfos.UNIT_LINE,1,endPoint="end")
				speech.speakTextInfo(end,reason=controlTypes.REASON_CARET)
				ui.message(_("Position: character %d") % bookmark)
				return
		ui.message(_("Next bookmark not found"))
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
			ui.message(_("No bookmarks found"))
			return
		start = obj.makeTextInfo(textInfos.POSITION_ALL)
		try:
			end = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			ui.message(_("Can not find bookmark"))
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
				ui.message(_("Position: character %d") % bookmark)
				return
		ui.message(_("Previous bookmark not found"))
	script_selectPreviousBookmark.__doc__ = _("Moves to the previousbookmark.")

	def script_copyCurrentBookmarksFile(self, gesture):
		try:
			fileName = self.getFile("bookmarks")
		except AttributeError:
			return
		if not api.copyToClip(os.path.basename(fileName)):
			ui.message(_("Cannot copy file name for place markers"))
			return
		ui.message(_("Place markers file name copied to clipboard"))
	script_copyCurrentBookmarksFile.__doc__ = _("Copies to the clipboard the name of current file for place markers.")

	__gestures = {
		"kb:control+shift+NVDA+s": "specificSave",
		"kb:control+shift+NVDA+f": "specificFind",
		"kb:control+shift+NVDA+k": "saveBookmark",
		"kb:control+shift+NVDA+delete": "deleteBookmark",
		"kb:control+shift+k": "selectNextBookmark",
		"kb:shift+NVDA+k": "selectPreviousBookmark",
		"kb:NVDA+k": "copyCurrentBookmarksFile",
	}

