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

a = tuple(range(0,10))

print(a)



## 아래와 같이 자료가 없는 형태로도 만들기도 함. 요소를 실수로 변경하는 상황을 방지하기 위해서
b = 1, 2, 4, 5, 7, 8, 10

print(b)

print((40, ))

print(30,)

    
print(list('Hello World'))

print(tuple('Hello World'))


a, b, c = [1, 2, 3]

print(a, b, c)