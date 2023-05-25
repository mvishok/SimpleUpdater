from os import system
from pathlib import Path
from subprocess import Popen
from .download import *
from .check import *

def checkForUpdates(CURRENT_VERSION, versionUrl):
    ver = versionFile(versionUrl)
    args = Path(ver).read_text().splitlines()
    NEW_VERSION = str(args[0])
    updaterUrl = str(args[1])

    if checkVersion(CURRENT_VERSION, NEW_VERSION) == True:
        updaterPath = updaterFile(updaterUrl)
        Popen(updaterPath)
        exit()