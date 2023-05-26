import urllib.request as req
import os.path
import tempfile

def versionFile(versionUrl):
    print("Checking for updates...")
    tempDir = tempfile.gettempdir()
    downloadPath = os.path.join(tempDir, 'ver.txt')
    try:
        req.urlretrieve(versionUrl, downloadPath)
        return downloadPath
    except Exception as e:
        print(e)
        exit()

def updaterFile(updaterUrl):
    print("Update found, downloading...")
    tempDir = tempfile.gettempdir()
    updaterPath = os.path.join(tempDir, 'updater.exe')
    try:
        req.urlretrieve(updaterUrl, updaterPath)
        return updaterPath
    except Exception as e:
        print(e)
        exit()
