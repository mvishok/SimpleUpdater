from packaging import version

def checkVersion(CURRENT_VERSION, NEW_VERSION):
    try:
        if version.parse(CURRENT_VERSION) < version.parse(NEW_VERSION):
            return True 
    except Exception as e:
        print(e)
        exit()
