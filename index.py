#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python
print("Content-Type: text/html", 'html lang="kor"')
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('../data/'+pageId, 'r').read() # '..'로 한 단계 상대경로를 통해서 한 단계 상위의 디렉토리를 찾음
else:
    pageId = 'Welcome'
    description = 'Hello , Web'  
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    <li><a href="index.py?id=Python">Python</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}<p>
</body>
</html>
'''.format(title=pageId,  desc=description))