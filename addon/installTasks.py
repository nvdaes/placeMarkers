# -*- coding: UTF-8 -*-

import addonHandler
import os
import shutil
import globalVars
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	configPath = globalVars.appArgs.configPath
	addonPath = os.path.join(configPath, "placeMarkersBackup")
	if not os.path.isdir(addonPath):
		return
	basePath = os.path.dirname(__file__)
	savePath = os.path.join(basePath, "globalPlugins", "placeMarkers")
	if gui.messageBox(_("Your configuration folder for NVDA contains files that seem to be derivated from a previous version of this add-on. Do you want to update it?"),
	_("Install or update add-on"),
	wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
		try:
			shutil.copytree(addonPath, savePath)
		except IOError:
			pass
