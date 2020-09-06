#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python

import os, html_sanitizer


def getlist():
    sanitizer = html_sanitizer.Sanitizer()
    files = os.listdir('../data/')
    listStr = ''
    for item in files:
      item=sanitizer.sanitize(item)
      listStr = listStr + '<li><a href="index1.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr