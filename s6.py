# a = 5
# b = 10

# print(a if a < b else b)
# тернарный оператор

# Задача 39
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 

# from random import randint
# # my_list = [randint(0, 10) for i in range(15)]
# my_list1 = list()
# lens = int(input("введите длину списка 1:"))
# for i in range(lens):
#     my_list1.append(randint(0, 15))
# print(my_list1)

# my_list2 = list()
# lens = int(input("введите длину списка 2:"))
# for i in range(lens):
#     my_list2.append(randint(0, 10))
# print(my_list2)

# my_list3 = []
# for i in my_list1:
#     if i not in my_list2:
#         my_list3.append(i)
       
# print(my_list3) 

# from random import randint
# f_list = [randint(0, 10) for i in range(15)]
# s_list = [randint(0, 10) for i in range(15)]

# print(f_list, s_list, sep='\n')
# print([item for item in f_list if item not in s_list])

# Задача 41
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного.

# from random import randint
# f_list = [randint(0, 10) for i in range(15)]
# print(f_list)
# count = 0
# for i in range(1, len(f_list)-1):
#     if f_list[i-1] < f_list[i] > f_list[i+1]:
#         count += 1
# print(count)

# from random import randint
# f_list = [randint(0, 10) for i in range(15)]
# print(f_list)
# count = 0
# for i in range(1, len(f_list)-1):
#     if f_list[i-1] < f_list[i] > f_list[i+1]:
#         count += 1
# if f_list[-1] < f_list[0] > f_list[1]:
#     count += 1
# if f_list[0] < f_list[-1] > f_list[-2]:
#     count += 1
# print(count)

# цикличность i%len
# from random import randint
# print(f_list := [randint(0, 10) for i in range(15)])

# count = 0
# for i in range(len(f_list)):
#     index = i % len(f_list)
#     if f_list[(i - 1)% len(f_list)] < f_list[i % len(f_list)] > f_list[(i + 1) % len(f_list)]:
#         count += 1

# print(count)

# задача 43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. 


# from random import randint
# # maximal = int(input('Введите максимальное число: '))
# # minimal = int(input('Введите минимальное число: '))
# # my_list = [randint(minimal, maximal) for i in range(10)]

# my_list = list()
# lens = int(input("введите длину списка:"))
# for i in range(lens):
#     my_list.append(randint(0, 10))

# print(my_list)
# counting = 0
# for i in range(1, 10 + 1):
#     counting += my_list.count(i) // 2
# print(counting)


# Задача 45
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. 

# list_ = []
# num = int(input('введите число: '))
# dict_ = dict()
# for i in range(1, num + 1):
#     sum_ = 0
#     for j in range(1, i // 2 + 1):
#         if not i % j:
#             sum_ += j
#     dict_[i] = sum_
# print(dict_)
# dict_2 = dict()
# for k, v in dict_.items():
#     for k1, v1 in dict_.items():
#         if k == v1 and k1 == v and k != k1 not in dict_2.keys():
#             dict_2[k] = k1

# print(dict_2)


# sum_div_num = {}
# for number in range(1, 10000):
#     sum_ = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sum_ += i
#     sum_div_num[number] = sum_

# for num in sum_div_num:
#     if num == sum_div_num.get(sum_div_num.get(num)) and num > sum_div_num.get(num):
#         print(num, sum_div_num.get(num))