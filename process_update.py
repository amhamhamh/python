#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python

import cgi, os
form = cgi.FieldStorage()
pageId= form["pageId"].value
title = form["title"].value
description = form["description"].value


opened_file=open('../data/'+pageId, 'w')
opened_file.write(description) # 10줄에 있는 거 다시 써줌
opened_file.close()

os.rename('../data/'+pageId, '../data/'+title)

#redirection(파일이 끝내고 다시 돌아올 위치). 여기 있는 내용들은 행동만 함. 
print("Location:create.py?id="+title)
print()