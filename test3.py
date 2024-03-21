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

import math

class Point2D:
    def __init__(self, x= 0, y = 0):
        self.x = x
        self.y = y
        
        
length =  0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]

p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())


for i in range(len(p) - 1):
    k =  math.sqrt(((p[i].x - p[i+1].x)**2) + ((p[i].y - p[i+1].y)**2))
    length += k
    print(k, length)
    
    
print(length)

