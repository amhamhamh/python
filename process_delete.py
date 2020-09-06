#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python

import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('../data/'+pageId)

print("Location:index1.py")
print()