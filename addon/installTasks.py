# -*- coding: UTF-8 -*-
# installTasks for placeMarkers add-on
# Copyright (C) 2016-2025 Noelia Ruiz Martínez, Łukasz Golonka
# Released under GPL 2

import addonHandler
import os
import shutil
import globalVars
from gui.message import MessageDialog, ReturnCode

addonHandler.initTranslation()


def copyTree(src, dst):
	try:
		shutil.copytree(src, dst)
	except IOError:
		pass


def onInstall():
	configPath = globalVars.appArgs.configPath
	addonDir = os.path.abspath(os.path.dirname(__file__))
	placeMarkersPath = os.path.join(addonDir, "globalPlugins", "placeMarkers", "savedPlaceMarkers")
	addonBackupPath = os.path.join(configPath, "placeMarkersBackup")
	if os.path.isdir(addonBackupPath):
		if (
			MessageDialog.ask(
				_(
					# Translators: label of a dialog presented when installing this addon and placeMarkersBackup is found.
					"Your configuration folder for NVDA contains files that seem to be derived from a previous version of"
					" this add-on. Do you want to update it?",
				),
				# Translators: title of a dialog presented when installing this addon and placeMarkersBackup is found.
				_("Install or update add-on"),
			)
			== ReturnCode.YES
		):
			copyTree(addonBackupPath, placeMarkersPath)
			return
	previousPlaceMarkersPath = os.path.join(
		configPath,
		"addons",
		"placeMarkers",
		"globalPlugins",
		"placeMarkers",
		"savedPlaceMarkers",
	)
	if os.path.isdir(previousPlaceMarkersPath):
		copyTree(previousPlaceMarkersPath, placeMarkersPath)
