from os import system
from pathlib import Path
from subprocess import Popen
import download
import check

def checkForUpdates(CURRENT_VERSION, versionUrl):
    ver = download.versionFile(versionUrl)
    args = Path(ver).read_text().splitlines()
    NEW_VERSION = str(args[0])
    updaterUrl = str(args[1])

    if check.checkVersion(CURRENT_VERSION, NEW_VERSION) == True:
        updaterPath = download.updaterFile(updaterUrl)
        Popen(updaterPath)
        exit()