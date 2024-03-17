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
# text_input  = input('숫자를 넣어주세요. ')

# int_array = [int(value) for value in text_input.split()]

# print('int_array : ',int_array, type(int_array[0]))


# a = [1.2, 2.5, 3.7, 4.6]

# for idx, val in enumerate(a):
#     print(f'{int(val) , int(a[idx])}')

# print(list(map(int, a)))

# a = (38, 21, 53, 62, 19, 53)
# k = a.index(62)
# print(k)

# a = (38, 21, 53, 62, 19)

# k = tuple(i for i in range(10) if i % 2 == 0)
# print(k)

# a = [38, 21, 53, 62, 19]
# a.append(40)
# print(a)


# a = [[10, 20], [30, 40], [50, 60]]

# print(a[0][0])

# print(a[1][0])

# a = []
# a.append([])
# a[0].append(10)
# a[0].append(13)
# a[0].append(15)
# a.append([])
# a[1].append(19)
# a[1].append(20)
# a[1].append(21)
# print(a)


# a = [[10, 20], [30, 40], [50, 60]]
# for x, y in a:
#     print(x, y)
    
# 반복 배열    
# for i in a:
#     for j in i:
#         print(j, end=' ')
        
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(f'a{[i]}{[j]} : {a[i][j]}')

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(f'a{[i]}{[j]} {a[i][j]}')

# i = 0

# while i < len(a):
#     j = 0  
#     while j < len(a[i]):
#         print(f'a{[i]}{[j]} {a[i][j]}')        
#         j += 1
#     i += 1    
#     print()
    


# a = []

# for i in range(10):
#     a.append(0)

# for i in range(3):
#     temp = []
#     # a.append(temp)
#     for j in range(2):        
#         temp.append(0)
#     a.append(temp)

# a = [[0 for j in range(2)] for i in range(3)]
# a = [[0] * 2 for j in range(3)]
# print(a)


# a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
# b = []    # 빈 리스트 생성

# for j in a:
#     temp = []
#     for i in range(j):
#         temp.append(0)
#     b.append(temp)
    
# print(b)

# a = [[0] * i for i in [3, 1, 3, 2, 5]]

# print(a)

# a = [[0] * i for i in [3, 1, 3, 2, 5]]

# a = [[10, 20], [30, 40]]
# import copy  

# c = a.copy() #  주소 복사, 참조
# b = copy.deepcopy(a) 
# b[0][0] = 500


# print(a)
# print(b)
# print(c)

# b = copy.deepcopy(a) # 값복사


# print(b)


# [
#     [
#         [0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0]
#     ], 
#     [
#         [0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0], 
#         [0, 0, 0]
#     ]

# ]

# k = [[0] * 3 for i in range(2) for j in range(4)]

# k = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]

# print(k)



# s = 'Hello, world!'
# s = s.replace('Hello', '헬로')
# print(s)

# table = str.maketrans('aeiou', '12345') #문자 바꾸기 maketrans
# 'apple'.translate(table)


# k =  'apple pear grape pineapple orange'
# j = k.split() # 공백을 기준으로 분리하여 리스트로 변환

# print(k)
# print(j)


# p = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
# print(p)

# k = '   Python  .  '.lstrip()
# print(k)

# p =', python.'.lstrip(',.')
# print(p)


# p = 'python'.ljust(10) # 왼쪽 정렬
# p1 = 'python'.rjust(10) # 오른쪽 정렬
# print(p1)


# p1 = ' 35'.zfill(6) #왼쪽부터 빈칸은 0으로 채움
# print(p1)

# o =  'apple pineapple'.find('pl') #해당 문자의 인덱스


# o =  'apple pineapple'.find('xy') # find에서 해당 문자열이 없으면 -1을 반환

# print(o)

## 어떤 문자를 찾는 것은 순서를 가져오는 것. find
## count('pl') -  이것은 해당 문자와 같은 값을 가져오는 것. 

# o = 'apple pineapple'.count('pl')
# print(o)

# o = 'I am %s' % 'keep'
# o = 'I am %d' % 12

# o = 'I am %f' % 2.1 # 기본적으로 소수점 6자리까지..
# print(o)

# o = 'I am %10s' % 'learner'  # 왼쪽부터 10칸을 비워놓고 오른쪽 정렬
# print(o)

# o = 'I am %10d' % 150
# print(o)

# o = '%-10s' % 'python' # 왼쪽부터 10칸 비워서
# print(o)

# o = 'Today is %d %s' % (3, 'm') # 왼쪽부터 10칸 비워서
# print(o)


# language = 'Python'
# version = 3.6
# print(f'{language} {version}')


# k = '{0:>10}'.format('10칸') # 10칸 비우기

# k = '%03d' % 1 # 숫자 갯수는 3개 
## 0자리수.소수점자리f
# k = '{0:03d}'.format(35)

# k = '%08.2f' % 3.6
# k = format(121987851943500, ',') # format(숫자, '구분자') 만약에 ','를 넣으면 자리수 3개로 나눌 수 있음. 
# k = '{0:>20}'.format(193570) # format(숫자, '구분자') 만약에 ','를 넣으면 자리수 3개로 나눌 수 있음. 
# path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# k = path.split('\\')

# print(k)
# print(k[-1])


# 리스트는 실제 데이터 보다 더 큰 메모리를 사용하는 반면, 튜플은 고정된 메모리를 사용
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.update(a=50) ## 해당 데이터를 수정하는 방법
# print(x)

# y = {1: 'one', 2: 'two'}
# y.update({1:'ONE', 2:'TWO'})
# y.update([[2, 'TWO'], [4, 'FOUR']])
# y.update([[2, 'TWO'], [3, 'THREE']])
# y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# y.pop('a')
# print(y)
# del y['a']
# print(y)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
#p = x.popitem() # 임의로 삭제하는 키-값 쌍을 튜플로 반환. 
# l = x.get('z', 0)
# l = x.items() # 키-값 쌍을 모두 가져옴. 
# c = x.keys() # 모든 키를 가져옴. 
# o = x.values() # 모든 키를 가져옴. 
# print(c, o)

# keys = ['a', 'b', 'c', 'd']
# # x = dict.fromkeys(keys)  # 해당 키 리스트를 딕셔너리로 생성하며, 모두 None 값으로 생성
# y = dict.fromkeys(keys)
# print(x)


# from collections import defaultdict
# y = defaultdict(int) 
# keys = ['a', 'b', 'c', 'd']
# y = dict.fromkeys(keys, 100) # dict
# print(y)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for i in x:
#     print(i, end=' ')
    
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items(): # 해당 아이템의 value의 값을 가져오는 것. 
#     print(key, value)


# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key in x.keys():
#     print(key, end=' ')

# print()
# for val in x.values():
#     print(val, end=' ')

# keys = ['a', 'b', 'c', 'd']
# x = {key: value for key, value in dict.fromkeys(keys).items()}

# x = {key:value for key, value in dict.fromkeys(keys).items()}
# x = {key: 0 for key in dict.fromkeys(keys).keys()}

# 삭제를 하는 것이 아니라, 제외하는 것
# x = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}


# 어떤 value 값을 삭제하는 것은 직접 키 값을 삭제하는 것이 아니라, 삭제할 key&value 값을 삭제하는 것임. 
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x = {key: value for key, value in x.items() if value != 20}
# x = {key:value for key, value in x.items() if value != 20}
# print(x)

# maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

# avg =  sum(maria.values()) / len(maria)
# print(avg)

## set은 집합. 
# a = set('apple')

# print(a)

# k = set('keep')
# print(k)

# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}
# b = {6, 7, 5, 9, 10}

## 합집합
# c = a | b
# c = set.union(a, b)
# a.update({5})

# 교집합
# c = a & b 
# c = set.intersection(a, b)

# 차집합
# c = a - b
# c = set.difference(a, b)
# c = set.difference(b, a)

# 대칭차집합
# c = a ^ b
# c = set.symmetric_difference(a, b)

# a = {1, 2, 3, 4}
# a |= {5}

# 교집합
# a = {1, 2, 3, 4}
# a &={1, 2, 3, 4, 5}


# print(a)


# a = {1, 2, 3, 4}
# a ^= {3, 4, 5, 6}


# a = {1, 2, 3, 4}
# a &= {0, 1, 2, 3, 4}

# 교집합 업데이트 
# a = {1, 2, 3, 4}
# a.intersection_update({0, 1, 2, 3, 4})

# print(a)

# 부분 집합
# a = {1, 2, 3, 4}
# 
# print(a <= {1, 2, 3, 4})
# 
# print(a.issubset({1, 2, 3, 4}))

# 진부분 집합(상위 집합인지)
# a = {1, 2, 3, 4}
# print(a < {1, 2, 3, 4, 5}) 

# 진상위집합인지
# a = {1, 2, 3, 4}
# print(a > {1, 2, 3}) 

# 세트가 같은지 다른지 확인하기
# a = {1, 2, 3, 4}
# print(a == {1, 2, 3, 4})

# a = {4, 3, 2, 1}
# print(a == {1, 2, 3, 4})

# a = {1, 2, 3, 4}
# print(a != {1, 2, 3})

# a = {1, 2, 3, 4}
# print(a.isdisjoint({5, 6, 7, 8})) # 겹치는 요소가 있는지 없는지
# print(a.isdisjoint({3, 4, 5, 6}))

# a = {1, 2, 3, 4}
# a.add(5)
# print(a)

# 특정요소 삭제
# a.remove(3)
# print(a)

# 모든 요소 삭제
# a.clear()
# print(a)

# a.pop()
# print(a)

# a.pop()
# print(a)

# 표현식으로 중복된 요소를 빼고 출력
# a = {i for i in 'apple'}
# print(a)

# 반복되지 않은 것에 대해서 표현
# a = {i for i in 'pineapple' if i in 'apl'}
# print(a)


# a = {i for i in range(0, 101) if i % 3 == 0}
# b = {i for i in range(0, 101) if i % 5 == 0}
# print(a & b)


#  a와 b의 공약수 구하기
# c, k = map(int, input().split(' '))
# a = {i for i in range(1, c+1) if c % i == 0} 
# b = {i for i in range(1, k+1) if k % i == 0} 

# print(a & b)

# file = open('hello.txt', 'w') # hello.txt 파일을 쓰기 모드로 열기, 파일 객체로 변환
# file.write('Hello world')
# file.close()

# file = open('hello.txt', 'w') # hello.txt 파일을 쓰기 모드로 열기, 파일 객체로 변환
# file.write('Hello world') # 파일을 문자열에 저장
# file.close()

# file = open('hello.txt', 'r')  #파일을 읽기모드로 열기
# s = file.read() # 안에 파일 내용 읽기
# print(s) # 값 출력
# file.close()

# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

## 파일 읽기 모드 및 쓰기 모드
# with open('hello.txt', 'r') as file:
    # s = file.read()
    # print(s)
    # for i in range(3): # 반복문을 돌면서 입력
    #     file.write(f'Hello world{i}\n') 
    # file.writelines(lines)
    # k = file.readlines()
    # print(k)

# 줄 읽기
# with open('hello.txt', 'r') as file:
#     line = None
#     while line != '': # 파일을 읽을 때 특정 조건 없이 계속 읽을 수 있음.
#         line = file.readline() # 파일의 내용을 한 줄씩 리스트 형태로 가져옴.
#         print(line.strip('\n'))    
    # lines = file.readlines()
    # print(lines)

# 파일 읽기
# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line.strip('\n'))


# 피클링 - 파이썬 객체를 파일에 저장하는 과정
# 언피클링 - 파일에서 객체를 읽어오는 과정
# import pickle

# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
# sex = 'male'

# with open('jame.p', 'ab') as file: # jame.p 파일을 바이너리 쓰기 모드로 변환
# with open('james.p', 'xb') as file: # jame.p 파일을 ㅈ
#     pickle.dump(sex, file)
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)

# 'a'는 추가 모드
# 'X'는 베타적 생성 - 파일이 이미 있으면 에러발생, 없으면 새로운 파일을 만듬
# 
# with open('james.p', 'rb') as file: # jame.p 파일을 바이너리 읽기 모드로 변환
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     sex = pickle.load(file)

# print(name)
# print(age)
# print(address)
# print(scores)
# print(sex)

with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for i in words:
        if len(i.strip('\n')) < 11:
            count += 1
    print(count)