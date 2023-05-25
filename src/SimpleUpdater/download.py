import urllib.request as req
import os.path
import tempfile

def versionFile(versionUrl):
    print("Checking for updates...")
    tempDir = tempfile.gettempdir()
    downloadPath = os.path.join(tempDir, 'ver.txt')
    req.urlretrieve(versionUrl, downloadPath)
    return downloadPath

def updaterFile(updaterUrl):
    print("Update found, downloading...")
    tempDir = tempfile.gettempdir()
    updaterPath = os.path.join(tempDir, 'updater.exe')
    req.urlretrieve(updaterUrl, updaterPath)
    return updaterPath
