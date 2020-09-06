#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python
user_id = input('id?')
user_pwd = input('password?')
'''
if user_pwd == '111111':
    print('Hello master')
else:
    print('Who are you?')
'''

'''
if user_id == 'egoing':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
'''

if user_id == 'egoing' and user_pwd == '111111': # and 연산자에 따라 두 개다 참일 때 print가 실행
    print('Hello master')
elif user_id == 'leezche' and user_pwd == '222': # else if문은 python에서 elif로 쓰여짐
    print('Hello master')
else:
    print('Who are you?')