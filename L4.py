# def f(x):
#     return x*x

# print(f(5))

# print(type(f))

# a = f
# print(type(a))

# print(a(5))

#  a хранит в себе ссылку на функцию а

# калькулятор

# def calk1(a):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk1, 5)

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 45)

# сокращение лямда функции

# def calk2(a, b):
#     return a + b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b:a + b

# math(calk1, 5, 45)

# math(lambda a,b:a + b, 5, 45)

# задача 1
# my_list = [1, 2, 3, 5, 8, 15,  23, 38]
# res = list()

# for i in my_list:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)



# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# my_list = [1, 2, 3, 5, 8, 15,  23, 38]
# res = select(int, my_list)
# print(res)
# res = where( lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)




# data = [1, 2, 3, 5, 8, 15,  23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# функция map функция и объект

# list_1 = [ x for x in range(1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10 , list_1))
# print(list_1)

# задача 2

# .split(', ')

# data = '15 156 96 3 5 8 52 5'

# # print(data)
# # data = data.split(', ')
# # print(data)


# data = list(map(int, data.split()))
# print(data)



# фильтр значений принимает два оргумента функция и объект возвращает тру

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# zip для итеррирумых объектов и возвращает итератор с картежом

# файлы

# colors = ['red', 'green', 'blue']
# data = open('file.text', 'a', ) # режим работы
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.text', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# print(56)

