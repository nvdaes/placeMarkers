# installTasks for placeMarkers add-on
# Copyright (C) 2016-2026 Noelia Ruiz Martínez, Łukasz Golonka
# Released under GPL 2

import addonHandler
import pickle
import yaml
import shutil
from pathlib import Path

from NVDAState import WritePaths
from gui.message import MessageDialog, ReturnCode

addonHandler.initTranslation()


def copyTree(src, dst):
	try:
		shutil.copytree(src, dst)
	except IOError:
		pass


class _NoteProxy:
	"""Placeholder class used when unpickling Note objects during migration."""

	title: str = ""
	body: str = ""


class _SafeUnpickler(pickle.Unpickler):
	def find_class(self, module, name):
		if name == "Note":
			return _NoteProxy
		raise pickle.UnpicklingError(f"Refusing to unpickle {module}.{name}")


def migratePickleToYaml(folder):
	"""Convert all .pickle bookmark files under folder to .yaml using safe_dump."""
	for pickleFile in Path(folder).rglob("*.pickle"):
		try:
			with open(pickleFile, "rb") as f:
				data = _SafeUnpickler(f).load()
			if isinstance(data, list):
				yamlData = {pos: {"title": "", "body": ""} for pos in data}
			elif isinstance(data, dict):
				yamlData = {}
				for pos, note in data.items():
					if isinstance(note, _NoteProxy):
						yamlData[pos] = {"title": note.title, "body": note.body}
					else:
						yamlData[pos] = {"title": "", "body": ""}
			else:
				continue
			yamlFile = pickleFile.with_suffix(".yaml")
			with open(yamlFile, "w", encoding="utf-8") as f:
				yaml.safe_dump(yamlData, f, allow_unicode=True)
			pickleFile.unlink()
		except Exception:
			pass


def onInstall():
	placeMarkersPath = (
		Path(addonHandler.getCodeAddon().path) / "globalPlugins" / "placeMarkers" / "savedPlaceMarkers"
	)
	addonBackupPath = Path(WritePaths.configDir) / "placeMarkersBackup"
	if addonBackupPath.is_dir():
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
			migratePickleToYaml(placeMarkersPath)
			return
	previousPlaceMarkersPath = (
		Path(WritePaths.configDir) / "addons" / "placeMarkers" / "globalPlugins" / "placeMarkers" / "savedPlaceMarkers"
	)
	if previousPlaceMarkersPath.is_dir():
		copyTree(previousPlaceMarkersPath, placeMarkersPath)
	migratePickleToYaml(placeMarkersPath)
