from SimpleUpdater import SimpleUpdater

# Current version of the application
CURRENT_VERSION = '1.0'

# URL to fetch the latest version information
VERSION_URL = 'https://example.com/version.txt'

SimpleUpdater.checkForUpdates(CURRENT_VERSION, VERSION_URL)

#...