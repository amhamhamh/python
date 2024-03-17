# 함수의 틀만 만들때 쓰는 것.
# def hello():
#     pass

# def add(a, b):
#     print(a+b)

# print(add(10, 20))


# ''' ''' -이거는 독트스트링으로 함수에 대한 메모를 남기는 것
# 함수이름.__doc__
# def add(a, b):
#     '''이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다.'''
#     return a+b

# print(add(10, 20))

# print(add.__doc__)

# def add(a, b):
#     return a+b

# print(add)


# def add_sub(a, b):
#     return a+b, a-b

# # x = add_sub(10, 20) - 해당 값은 튜플로 변환. 괄호없이 하면 튜플 
# x, y = add_sub(10, 20)
# print(x, y)

# def one_two():
#     # return (1, 2)
#     # return 1, 2
#     return [1, 2]

# a, k = one_two()
# # print(one_two())
# print(a, k)


# 나눗셈 연산자 // 를 사용, 나머지 연산자는 % 사용
# def get_quotient_remainder(x, y):
#     return x // y, x % y

# def personal_info(name, age, address):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)

# x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# print(personal_info(**x)) # 딕셔너리 언패킹함. - value 값을 할당함.
# print(personal_info(*x)) # 딕셔너리 언패킹함. - 일반 key값을 가지고 옴.

# 가변 변수 **kwargs 를 사용하여 함수 입력

# def personal_info(**kwargs):
#     '''개인 정보를 표현하는 함수'''
#     for kw, arg in kwargs.items():
#         print(f'{kw} : {arg}')

# print(personal_info(name='홍길동'))
# x = {'name': '홍길동', 'age': 15, 'address': '동부 이촌동'}
# print(personal_info(**x))        

# print(personal_info(name='홍길동', age=15, address='포항시 남구 대도동'))

# def personal_info(**kwargs):
#     if 'name' in kwargs:
#         print('이름', kwargs['name'])

# def personal_info(name, **kwargs):
#     print(name)
#     print(kwargs)

# personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
# personal_info('홍길동', **{'age': 30, 'address': '서울시 용산구 이촌동'})
# personal_info(**{'name':'홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# korean, english, mathematics, science = 100, 86, 81, 91

# def get_max_score(*args): # 에스터리스크
#     return max(args)

# max_score = get_max_score(korean, english, mathematics, science)
# print('높은 점수:', max_score)

# max_score = get_max_score(english, science)
# print('높은 점수:', max_score)