import os
import subprocess as sp

paths = {
    'visual studio code': 'C:\\Users\\bettc\\AppData\Local\Programs\\Microsoft VS Code\\code.exe',
    'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_chrome():
    os.startfile(paths['chrome'])


def open_cmd():
    os.system('start cmd')
