# объекты через подчеркивание 
# классы с больших букв

# while - цикл
# for - перебор

# Задача 1 факториал числа через цикл
# n = int(input('введите n '))
# i = 1
# factorial = 1
# while i <= n:
#     factorial = factorial * i
#     i += 1
# print(factorial)

# Задача 2 
# каким по # счету числом Фибоначчи является число 
# number = int(input('введите  '))
# i = 3
# f_one = 0
# f_two = 1
# answer = f_one + f_two
# while answer < number:
#     f_one = f_two
#     f_two = answer
#     answer = f_one + f_two
#     i += 1
# print(answer)
# if number == answer:
#     print(i)
# else:
#     print(-1)

# Задача 3 мах и min вес арбузов

# from random import randint
# for _ in range(10):
#     print(randint(0, 50))

# from random import randint
# count = int(input('введите количество арбузов '))
# min = 11 
# max = 0
# # min = float("inf")
# # max = float("-inf")
# for i in range(count):
#     weight = (randint(1, 10))
#     print('вес арбуза', weight)
#     # if weight < min:
#     #     min = weight     
#     # if weight > max:
#     #     max = weight
#     if weight > max:
#         max = weight     
#     if weight < max and weight < min:
#         min = weight
# print('самый тяжелый арбуз - ', max)
# print('самый легкий арбуз - ', min)

# Задача 4 

#  st = 1 + increse = random (-3 , 3)

# from random import randint
# days = int(input('введите количество дней '))
# temp = 1
# count = 0
# total_days = 0
# for i in range(days):
#     temp = temp + randint(-3, 3)
#     print(temp)
#     if temp > 0:
#         count += 1
#     else:
#         count = 0

#     if total_days < count:
#         total_days = count 

# print(total_days)
