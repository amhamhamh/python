#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!pythons
s =[1, 'four', 5, 16]
print(s)
print(s[0])
s[1] = 4
print(s)
del s[2] # del 명령은 list 안에 있는 해당 인자를 삭제함
print(s)
s.append(10) # append 명령은 list 끝에 있는 젤 끝에 있는 인자를 추가시킴(단, 하나의 인자만)
print(s)
f=[17,18]
s.extend(f) # extend 명령은 list 끝에 만약 배열일 경우 각 인자를 개별적으로 추가시킴
print(s)
g=[19,20]
s.append(g) 
# 이럴 경우에는 append 명령은 list g를 아예 인자로 받아들여, 결과 값은 
# [1,4,16,10,17,18,[19,20]]
print(s)
umc = {'name':"myeongheon", 'age':'33'} #여기에서 name과 age는 dictionery에 해당하는 값. (JS에서 key 값은 name. myeongheon는 value 값 해당)
print(umc['name'])   
print(umc['name'].capitalize()) # capitalize()는 해당 값의 첫 글자를 대문자화 시키는 것을 의미함. 
