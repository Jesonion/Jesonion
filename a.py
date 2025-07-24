import os
import winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
shortcut_path = os.path.join(desktop, "百度.url")

with open(shortcut_path, 'w') as shortcut:
    shortcut.write('[InternetShortcut]\n')
    shortcut.write('URL=https://www.baidu.com\n')
