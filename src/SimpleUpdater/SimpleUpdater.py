from os import system
from pathlib import Path
from subprocess import Popen
from .download import *
from .check import *

def checkForUpdates(CURRENT_VERSION, versionUrl):
    ver = versionFile(versionUrl)
    args = Path(ver).read_text().splitlines()
    NEW_VERSION = str(args[0])
    updateType = str(args[1])
    updaterUrl = str(args[2])

    if checkVersion(CURRENT_VERSION, NEW_VERSION) == True:
        updaterPath = updaterFile(updaterUrl)

        if updateType == "normal":
            from easygui import ynbox
            if ynbox('An update for the application is available. Would you like to download and install it?', 'Update Available', ('Yes, Download Now', 'No, Remind Me Later')):
                Popen(updaterPath)
                exit()
        elif updateType == "important":
            from easygui import ynbox
            if ynbox('An important update for the application is available. This update contains critical bug fixes and security enhancements. It is mandatory to download and install the update to ensure the continued functionality and security of the application.', 'Important Update Required', ('Download Now', 'Exit Application')):
                Popen(updaterPath)
                exit()
            else:
                exit()
        elif updateType == "silent":
            Popen(updaterPath)
            exit()