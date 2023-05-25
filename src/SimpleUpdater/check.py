from packaging import version

def checkVersion(CURRENT_VERSION, NEW_VERSION):
    if version.parse(CURRENT_VERSION) < version.parse(NEW_VERSION):
       return True 
