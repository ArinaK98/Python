# Задача 16. 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 

# from random import randint
# my_list = list()
# lens = int(input("Введите количество элементов :"))
# for i in range(lens):
#     my_list.append(randint(0, 10))
# print(my_list)
# number = int(input("Введите число, которое будем искать:"))
# count = 0
# for i in range(lens):
#     if my_list[i] == number:
#         count += 1
# print("Число", number, "встречается", count , "раз.")

# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.

# from random import randint
# my_list = list()
# lens = int(input("Введите количество элементов :"))
# for i in range(lens):
#     my_list.append(randint(0, 10))
# print(my_list)
# number = int(input("Введите число, самы близкий элемент которого будем искать:"))
# diff = abs(number - my_list[0])
# for i in range(lens):
#     if diff > abs(number - my_list[i]) and (abs(number - my_list[i])!= 0): 
#         diff = abs(number - my_list[i])
#         item = i+1
# print("Самый близкий к числу", number, "элемент - ", item)

