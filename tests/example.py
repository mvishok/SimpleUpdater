#0.0.1
import sys
print (sys.argv[1:])

# Current version of the application
CURRENT_VERSION = '0.0.1'

# URL to fetch the latest version information
VERSION_URL = 'http://localhost/file/ver.txt'

SimpleUpdater.checkForUpdates(CURRENT_VERSION, VERSION_URL)

#...
