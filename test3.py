# 37 두 점 사이의 거리 구하기

import math
import collections

# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        

# p1 = Point2D(x=30, y=20)
# p2 = Point2D(x=60, y=50)


# print(f'{p1.x}, {p2.x}')
# print(f'{p1.y}, {p2.y}')

# a = p2.x - p1.x
# b = p2.y - p1.y

## 직각 삼각형 빗변의 길이 
# c = math.sqrt((a * a)+(b * b))


# 거듭제곱
# c = math.sqrt(math.pow(a, 2)+math.pow(b, 2))

# print(c)


# Point2D = collections.namedtuple('Point2D', ['x', 'y']) # namedtuple로 점 표현

# p1 = Point2D(x= 30, y=20)
# p2 = Point2D(x= 60, y=50)

# a = p2.x - p1.x
# b = p2.y - p1.y

# c = math.sqrt((a * a) + (b * b))

# print(c)


# class Rectangle:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
        

# rect = Rectangle(x1=20, y1=20, x2=40, y2=30)


# a = abs(rect.x2 - rect.x1)
# b = abs(rect.y2 - rect.y1)

# width = a * b

# print(width)


# 사각형 변의 길이 구하기
# import math

# class Point2D:
#     def __init__(self, x= 0, y = 0):
#         self.x = x
#         self.y = y
        
        
# length =  0.0
# p = [Point2D(), Point2D(), Point2D(), Point2D()]

# p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())


# for i in range(len(p) - 1):
#     k =  math.sqrt(((p[i].x - p[i+1].x)**2) + ((p[i].y - p[i+1].y)**2))
#     length += k
#     print(k, length)
    
    
# print(length)

# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드



# y = [10, 20, 30]

# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)   
# except ZeroDivisionError as e: # 에러 메시지 출력5
#     print('0으로 나눌 수 없습니다.', e)
# except IndexError as e:
#     print('잘못된 인덱스 입니다.', e)

# try:
#     x = int(input('나눌 숫자를 입력하세요:'))
#     y = 10 / x
# except ZeroDivisionError:
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:
#     print(y)
# finally:
#     print('코드 실행이 끝났습니다.')

# try:
#     x = int(input('3의 배수를 입력하세요'))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.') # 예외 메시지를 지정해서 넣을 수 있음.
# except Exception as e: # 에러 자체를 지정할 수 있음.
#     print('예외가 발생하였습니다', e)

# def three_mutiple():
#     x = int(input('3의 배수를 입력해주세요'))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.') # 해당 코드에서 예외를 발생시킴. Exception을 만날 떄까지 올라가서 실행시킴 
#     print(x)

# try:
#     three_mutiple()
# except Exception as e:
#     print('에러 처리를 합니다. 메시지 : ', e)

# def three_mutiple():
#     try:
#         x = int(input('3의 배수를 입력해주세요'))
#         if x % 3 != 0:
#             raise Exception('3의 배수가 아닙니다.') # 해당 코드에서 예외를 발생시킴. Exception을 만날 떄까지 올라가서 실행시킴 
#     except Exception as e:
#         print('three_mutiple 함수에서 예외가 발생하였습니다.', e) # 여기에서 예외1
#         raise

# try:
#     three_mutiple()
# except Exception as e:
#     print('스크립트 파일에서 예외가 발생하였습니다', e) # 여기에서 예외2


# 객체 예외 확인
# class NotThreeMultipleError(Exception): # Exception 클래스를 상속 받아서, 새로운 예외 클래스를 만듦
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.') # 부모 클래스(Exception)의 메소드를 사용함

# def three_mutiple():
#     try:
#         x = int(input('3의 배수가 아닙니다.'))
#         if x % 3 != 0:
#             raise NotThreeMultipleError # 새롭게 만든 예외 객체를 사용하여 예외를 시킴
#     except Exception as e:
#         print('예외가 발생하였습니다', e)

# three_mutiple()


# print(dir([1, 2, 3])) # dir를 누르면 사용 가능한 객체의 메소드를 확인할 수 있음
# iterator는 값을 차례대로 꺼낼 수 있는 객체를 얘기함. (리스트, 딕트, 튜플..)
# 보통 이터레이터만 생성만 하고, 필요한 시점에서 불러써 씀(메모리를 아낌) - 지연 평가

# it = [1, 2, 3].__iter__()
# print(it.__next__()) # 요소를 다음 요소를 호출할 수 있음,.
# print(it.__next__())
# print(it.__next__())
# print(it.__next__()) # 뽑을 요소가 없을 때 저렇게 나옴.StopIteration

# 반복가능한 객체는 리스트, 문자, 튜플, 문자열, 딕셔너리, 세트
# 시퀀스(순서가 있는 객체) - 리스트, 문자, 튜플, 문자열. (딕셔너리와 세트는 예외 - key,val 값이 있는데- 이거는 순서가 있는 게 아니기 때문)



# 클래스에 직접 이터레이터와 __next__를 넣음
# class Counter:
#     def __init__(self, stop):
#         self.current = 0
#         self.stop = stop
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < self.stop:
#             r = self.current
#             self.current += 1
#             return r
#         else:
#             raise StopIteration

# for i in Counter(3):
#     print(i, end=' ')

# _, b = range(2) # '_'에 표현하는 것은 특정 순서에 반환값을 사용하지 않겠다는 관례적인 표현
# print(_, b)


# # 언패킹하여 특정 값을 사용하겠다는 의미임.
# a, _, c, d = range(4)
# print(_)


# Counter에 따라서 인덱스 값을 가져옴. 
# class Counter:
#     def __init__(self, stop):
#         self.stop = stop
    
#     def __getitem__(self, index):
#         if index < self.stop:
#             return index
#         else:
#             raise IndexError

# # print(Counter(3)[0], Counter(3)[1], Counter(3)[2]) # 인덱스만으로도 값을 가지고 올 수 있음


# for i in Counter(3):
#     print(i, end=' ')

# x = iter(range(3))   # 이터레이터 객체로 만듦
# print(x.__next__()) # 다음 값을 가지고 옴.
# print(x.__next__()) # 다음 값을 가지고 옴.
# print(x.__next__()) # 다음 값을 가지고 옴.
# print(x.__next__())


import random
# iter(반복할 객체, 반복을 끝낼 값) - 파이썬 내장함수 (이터레이터를 만들 객체)

# x = iter(lambda : random.randint(0, 5), 2)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# next(반복할 객체, 기본값) - 파이썬 내장함수(다음 값을 불러옴)

# it = iter(range(3))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10)) # StopIteration을 하지 않고, 기본값을 불러옴.
# print(next(it, 10))


# class MultipleIterator:
#     def __init__(self, stop, multiple):
#         self.stop = stop
#         self.mutiple = multiple
#         self.current = 0
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.current += 1
#         if self.current * self.mutiple < self.stop:
#             return self.current * self.mutiple
#         else:
#             raise StopIteration
        
# for i in MultipleIterator(30, 5):
#     print(i, end=' ')


# yield라는 키워드를 쓰면 그것이 제너레이터
# def number_generator():
#     yield 0 # 값(변수)를 지정하여 함수 바깥으로 전달. 실행을 양보??
#     yield 1 # 값(변수)를 지정하여 함수 바깥으로 전달. 실행을 양보??
#     yield 2 # 값(변수)를 지정하여 함수 바깥으로 전달. 실행을 양보??

# for i in number_generator():
#     print(i)


# 인덱스 범위가 넘어갈 경우  return(함수를 끝내는 것)- 이 값을 예외 값으로 던짐
# def one_generator():
#     yield 1
#     return 'return에 지정한 값'

# try:
#     g = one_generator()
#     next(g)
#     next(g)
# except StopIteration as e:
#     print(e)    # return에 지정한 값


# 해당 문자열을 대문자로 모두 출력
# def upper_generator(x):
#     for i in x:
#         yield i.upper()

# fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']

# for i in upper_generator(fruits):
#     print(i)
    

# yield from
# def number_generator():
#     x = [1, 2, 3]
#     # for i in x:
#     #     yield i
#     yield from x # 리스트에 들어 있는 요소를 한 개씩 세번 바깥으로 전달

# for i in number_generator():
#     print(i)

# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n # 변수를 바깥으로 던짐
#         n += 1

# def three_generator():
#     yield from number_generator(3) # 숫자를 세 번 바깥으로 전달함. 

# for i in three_generator():
#     print(i)

# 제네레이터 표현식
#(식 for i in 반복가능한객체)
#(i for i in 100)


# 데코리에터 @ - 함수를 장식하는 거
# def trace(func):
#     def wrapper():  # 호출할 함수를 감싸는 함수
#         print(func.__name__, '함수 시작')
#         func()
#         print(func.__name__, '함수 끝')
#     return wrapper # 함수를 반환하는 클로저

# @ trace # 함수를 수정하지 않은 상태에서 추가 기능.
# def hello():
#     print('hello')

# @ trace # 함수를 수정하지 않은 상태에서 추가 기능.
# def world():
#     print('world')

# # trace_hello = trace(hello)
# # trace_hello()
# # trace_world = trace(world)
# # trace_world()
    
# hello()
# world()

# 데코레이터
# def decorator1(func):
#     def wrapper():
#         print('decorator1')
#         func()
#     return wrapper

# def decorator2(func):
#     def wrapper():
#         print('decorator2')
#         func()
#     return wrapper

# # 데코레이터를 적용을 했을 때
# # @ decorator1 
# # @ decorator2
# def hello():
#     print('hello')

# # hello()

# decoratored_hello = decorator1(decorator2(hello))
# decoratored_hello()


# 매개변수가 있는 함수 데코레이터
# def trace(func):
#     def wrapper(a, b):
#         r = func(a, b)
#         print(f'{func.__name__} a: {a} b: {b} r:{r}')
#         return r
#     return wrapper
# @trace
# def add(a, b):
#     return a+b

# print(add(10 ,20))


# 단 애스터리스크와 쌍 애스터리크로 매개변수를 여러개를 받음. 
# def trace(func):
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs)
#         print(f'{func.__name__} arg -{args}, kwargs - {kwargs} r:{r}')
#         return r
#     return wrapper

# @trace
# def get_max(*args):
#     return max(args)

# @trace                   
# def get_min(**kwargs):   
#     return min(kwargs.values())

# print(get_max(10 ,20))
# print(get_min(x=10 ,y=20, z=30))


# def trace(func):
#     def wrapper(self, a, b): # 호출할 함수가 인스턴스 메서드이므로 첫번째 메소드는 무조건 self로 지정
#         r = func(self, a, b) # self와 매개변수를 그대로 넣어줌.
#         print(f'{func.__name__} a:{a}, b:{b}, r:{r}') # 매개변수와 변환값 출력
#         return r
#     return wrapper

# class Calc:
#     @trace
#     def add(self, a, b): # add는 인스턴스 메서드
#         return a + b

# c = Calc()
# print(c.add(10, 20))


# def is_mutiplet(x):
#     def real_decortor(func):
#         def wrapper(a, b):
        