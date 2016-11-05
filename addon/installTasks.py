# -*- coding: UTF-8 -*-
# installTasks for placeMarkers add-on
#Copyright (C) 2016 Noelia Ruiz Martínez
# Released under GPL 2

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
	if gui.messageBox(
	# Translators: label of a dialog presented when installing this addon and placeMarkersBackup is found.
	_("Your configuration folder for NVDA contains files that seem to be derived from a previous version of this add-on. Do you want to update it?"),
	# Translators: title of a dialog presented when installing this addon and placeMarkersBackup is found.
	_("Install or update add-on"),
	wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
		addonDir = os.path.dirname(__file__)
		placeMarkersPath = os.path.join(addonDir, "globalPlugins", "placeMarkers", "savedPlaceMarkers")
		try:
			shutil.copytree(addonPath, placeMarkersPath)
		except IOError:
			pass
