#!c:\users\joshua\desktop\codingstuff\lahacks\.virtualenvs\djangodev\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'channel==0.1.0','console_scripts','channel'
__requires__ = 'channel==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('channel==0.1.0', 'console_scripts', 'channel')()
    )
