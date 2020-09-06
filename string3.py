#!C:\Users\amham\AppData\Local\Programs\Python\Python38-32\python.exe
#!python
#positioning(데이터 안에 변수를 넣어서 바꾸어서 할당)
name = 'egoing'
age = 'one'
print('to '+name+'. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. '+name+' Duis aute irure dolor in '+age+' reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui '+name+' officia deserunt mollit anim id est laborum.')
#positional formatting('{} {}'.format('egoing', 12))- 문자열 안에 포맷을 넣어서, 일정한 형태로 변화하게 함
print('to {}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {} Duis aute irure dolor in {} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {} officia deserunt mollit anim id est laborum.'.format('egoing', 12, 'egoing', 'egoing'))
 
#Named placeholder('{first} {last}'.format(first='Hodor', last='Hodor!'))- 포맷을 이름 넣어서 지정함.
#그리고 last 안의 포맷 형식에 ex) first : digit 을 넣는다고 가정을 하면, 그 형태 외에는 실행이 안 됨.
print('to {name}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {age:digit} Duis aute irure dolor in {name} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {name} officia deserunt mollit anim id est laborum.'.format(name='egoing', age=12))
