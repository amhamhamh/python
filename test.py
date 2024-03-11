# a, b = map(int, input('숫자 두 개를 입력하세요 : ').split(','))
# print(a+b)

# a, b, c, d = map(str, input('문자를 입력해주세요 : ').split(' '))
# print(a, b, c, d)

# print(1, 2, 3, sep='*')

# print(1920, 1080, sep='X')

# print('대한민국', end='')
# print('사람입니다', end='')
# print('!!')


# print('Hello\nPython')

# print(int(5.5//2))


# year = 2000
# month = 10
# day = 27
# hour = 11
# minute = 43
# second = 59

# print(year, month, day, sep='/', end= ' ')
# print(hour, minute, second, sep=':')



# year, month, day, hour, minute, second = input().split()


# print(year, month, day, sep='-', end='T')
# print(hour, minute, second, sep=':')

# print(hour, minute, second, sep=':')

# import sys
# print(sys.getrefcount(1000)) # 레퍼런스한 횟수 카운트

# x = 1000
# print(sys.getrefcount(1000))


# y = 1000
# print(sys.getrefcount(1000))


# print(x is y)

# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a @ b, sep=' , ')


#print(False and 'Python')


# a = list(range(10))
# 
# print(a)
# 
# 
# b = list(range(5, 12))
# 
# print(b)

# c = list(range(-10, 10, 3))

# print(c)


# d = list(range(10, -4 ,-2))

# print(d)


## () 형태를 tuple이라고 함. 읽기 전용 리스트로 변경, 추가, 삭제 등이 불가함.

# a = tuple(range(0,10))

# print(a)



## 아래와 같이 자료가 없는 형태로도 만들기도 함. 요소를 실수로 변경하는 상황을 방지하기 위해서
# b = 1, 2, 4, 5, 7, 8, 10

# print(b)

# print((40, ))

# print(30,)

    
# print(list('Hello World'))

# print(tuple('Hello World'))


# a, b, c = [1, 2, 3]

# print(a, b, c)


# a = [1, 2, 3]
# print(a)
# a = tuple(a)
# print(a)


# x, y, z= a

# print(x, y, z)

# b = (4, 5, 6)
# print(b)
# b = list(b)
# print(b)


# a = [1, 2, 3] # 리스트 패킹
# b = (1, 2, 3) # 튜플 패킹
# c = 1, 2, 3 # 튜플 패킹


# a = input(int()).split(",")

# print(type(a[0]))
# print(len(a))

## 문맥 이해
# [expression for item in iterable if condition]



# text_input  = input('숫자를 넣어주세요. ')

# int_array = [int(value) for value in text_input.split()]

# print('int_array : ',int_array, type(int_array[0]))

# score_py=dict(math=80, english=95, science=80)

# print(score_py)

# dict_1 = ['제목1', '제목2', '제목3']
# dict_2 = [12, 13, 44]


# # zip 함수는 반복가능한 인자들을 매개변수로 받아서, 짝을 짓어주는 것을 말함. 
# dict_array = dict(zip(dict_1, dict_2))
# print(dict_array)

# keep = dict([('english', 150), ('math', 88), ('sceince', 18) , ('keep', 13)])


# print(keep)

# lux = dict(zip(['beckam', 'rohnaldo', 'melee'], [100, 200, 300]))

# print(lux)

# origin_dict = dict({'bechkam': 10, 'mana':334, 'melle':550, 'armor':500})
# print(origin_dict)


# lux={'health':490, 'mana':334, 'melee':500, 'armor':18.72, 'mana_regen':3.28}
# lux['plus_region'] = 440
# # print(lux['health'])

# print('health' in lux)

# x = 10

# if x == 10:
#     print('10입니다')

x = 5

# if x is not 10:
#     print('Ok')


# if x == 10:
#     print('10입니다.')
# else:
#     print('10이 아닌 숫자입니다.')


# if 0 < x < 10:
#     print('0에서 10 안에 있는 숫자입니다.')
# else:
#     print('0에서 10 안에 있는 숫자가 아닙니다.')

# writtten_test = 75
# coding_test = True

# if writtten_test >= 80 and coding_test  == True:
#     print('합격')
# else:
#     print('불합격')


# button = int(input())

# if button == 1:
#     print('3콜라')
# elif button == 2:
#     print('환타')
# elif button == 3:
#     print('사이다')
# else:
#     print('제공하지 않는 메뉴')

# x = int(input())

# if 11 <= x <= 20:
#     print('11~20')
# elif 21 <= x <= 30:
#     print('21~30')
# else:
#     print('아무것도 해당하지 않음')


# age = int(input())

# balance = 9000

# child = 650
# teenager = 1050
# adult = 1250


# if 7 <= age <= 12:
#     balance = balance-child
# elif 13<= age <= 18:
#     balance = balance-teenager
# elif age >= 19:
#     balance = balance-adult

# print(balance)

# formating. 자바스크립트의 template literal과 비슷한 것
# f스트링
# # str.format() 메서드
# for i in range(101):
#     # print(f"순서 :  {i}")
#      print("순서 %d :" % (i))


# name = 'jane'
# age = 28

# %를 사용하여 포매팅
# greeting = "Hello I'm %s. My age is %d" %(name, age) 


# format를 사용하여 포매팅
# greeting = "Hello I'm {}. My age is {}" .format(name, age)
# greeting = f"Hello I'm {name}. My age is {age}"

# print(greeting)

# for i in range(5, 12):
#     print('Hello, world!', i)

# for i in range(0, 10, 2):
#     print(f'Hello, world {i}')


# for i in range(10, 0, -1):
# for i in reversed(range(10)):
#     print(f'Hello world {i}')

# count = int(input('반복할 횟수를 적으세요'))

# for i in range(count):
#     print(f'반복할 숫자는 : {i}')

# letter = 'python'

# for i in reversed(letter):
#     print(i, end=" ")


# x = [49, -17, 25, 102, 8, 62, 21]

# for i in x:
#     print(i * 10, end=' ')

# x = int(input('숫자를 입력하세요 :'))

# for i in range(1, 10):
#     print(f'{x} * {i} = {x*i}')

# i = 0
# while i < 100:
#     print(f'숫자 : {i}')
#     i += 1

import random

# i = 0
# while i != 3:
#     i = random.randint(1, 10)
#     print(i)

# dice = [1, 2, 3, 4, 5, 6]

# print(random.choice(dice))

# i = 2 
# j = 5

# while i <= 32 or j >= 1:
#     print(i, j)
#     i *= 2
#     j -= 1

# x = int(input())

# while x >= 1350:    
#     x = x - 1350
#     print(x)
    


# for i in range(20):
#     if i % 2 == 0:
#         pass # 아무일도 하지 않음.
#     print(i)

# i = 0

# while True:
#     if i%10 != 3:
#         i += 1
#         continue
#     if i > 73:
#         break
#     print(i, end= ' ')


# start, stop = map(int, input().split())
 
# i = start
 
# while True:
#     # if start > stop:
#     #     break
#     if i % 10 == 3:
#         i += 1
#         continue
#     if i > stop:
#         print()
#         break
#     print(i, end= '/')
#     i += 1


# x = 5
# y = 0
# if x == 10:
#     y == x
# else:
#     y = 0

# if '':
#     print('참')
# else:
#     print('거짓')

# written_test = 75
# coding_test = True

# if written_test >=80 and coding_test == True:
#     print('합격')
# else:
#     print('불합격')

# korean, english, math, science = map(int, input().split())

# if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100 and 0 <= science <= 100:    
#     if (korean+english+math+science)/4 >= 80:
#         print('합격')
#     elif (korean+english+math+science)/4 < 80:
#         print('불합격')
# else: 
#     print('잘못된 점수')

# for i in range(0, 10, 2):
#     print('Hello, world!', i)

# for i in reversed(range(10, 21)):
#     print(i)



# for i in x:
#     print(i * 10, end=' ')

# x = [49, -17, 25, 102, 8, 62, 21]

# for idx, val in enumerate(x): ## enumerate 는 idx, val 값을 가지고 들고옴.
#     print(f'{idx} // {val * 10}', end=' [] ')
#     if idx == len(x) - 1:
#         print(f'{idx == len(x)-1}')

# for index, value in enumerate(x, start=1): ## 시작인덱스
#     print(index, value)

# a = [38, 21, 53, 62, 19]

# i = 0

# while i < len(a):
#     print(a[i])
#     i += 1

# a = [38, 3, 53, 62, 19]

# smallest_digit = a[0]

# for idx, val in enumerate(a):
#     if val < smallest_digit:
#         smallest_digit = val

# print(smallest_digit)

# x= list()
# x = map(int, input().split())

# print(x)


# x = list(range(0, 10))

# print(min(x))

##  리스트 컴프리헨션
# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)

# k = [i for i in range(0, 10)]

# k = list(i for i in range(0, 10))

# print(k)
# c = [i + 5 for i in range(10)]
# print(c)



# x = [i for i in range(10) if i % 2 == 0]
# x = list()
# for i in range(10):
#     if i % 2 == 0:
#         x.append(i)

# print(x)

## 리스트 표현식은 끝에서 앞으로 
a = [i * j for j in range(2, 10) for i in range(1, 10)]


