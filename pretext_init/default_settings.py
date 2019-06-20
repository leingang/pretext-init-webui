DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
LOG_DIR = '.'  # create log files in current working directory
SECRET_KEY = 'you-need-to-be-writing-beezercode'
# Licenses
# array of dicts.  The keys of each dict are:
# * title: (full) title of the license
# * identifier: (short) initialism
# * uri: URI/URL of the license
LICENSES = [
    {'title': 'Attribution-ShareAlike 2.0 Generic',
     'identifier': 'CC BY-SA 2.0',
     'uri': 'https://creativecommons.org/licenses/by-sa/2.0/'},
    {'title': 'Attribution-NonCommercial-ShareAlike 2.0 Generic',
     'identifier': 'CC BY-NC-SA 2.0',
     'uri': 'https://creativecommons.org/licenses/by-nc-sa/2.0/'},
    {'title': 'GNU Free Documentation License',
     'identifier': 'GFDL',
     'uri': 'https://www.gnu.org/licenses/fdl-1.3.en.html'},
]