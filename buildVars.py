# -*- Encoding: UTF-8 -*-
# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name
	"addon-name" : "placeMarkers",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Place markers"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("Add-on for setting place markers on specific virtual documents"),
	# version
	"addon-version" : "1.0-beta",
	# Author(s)
	"addon-author" : "Noelia <nrm1977@gmail.com>, Chris <llajta2012@hotmail.com>",
	# URL for the add-on documentation support
	"addon-url" : "http://www.wuala.com/programas%20para%20ciegos/Complementos%20para%20NVDA/add-ons/"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "*.py"), os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
