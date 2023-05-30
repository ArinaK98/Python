### Списки и словари
# списки и массивы не одно и то же
# массив содержит определенный тип данных
# список может состоять из чего угодно

# заполнение списка
# import random
# from random import randint
# my_list = []
# for _ in range(10):
#     my_list.append(random.randint(0,10))
# print(my_list)

# # my_list = set(my_list)
# # print(my_list)
# # print(len(my_list))

# uniq_list = []
# for item in my_list:
#     if item not in uniq_list:
#         uniq_list.append(item)
# print(uniq_list)
# print(set(my_list))
# print(list(set(my_list)))

# from random import randint
# lis = list()
# lens = int(input("введите длину списка:"))
# for i in range(lens):
#     lis.append(randint(0, 50))
# print(lis)

# numbers = 0
# for i in range(len(lis)):
#     for j in range(len(lis)):
#         if i != j:
#             numbers += 1
# print(numbers)

# my_string = ['qwqwqw']
my_string = 'qwqwqw'
print(my_string)
my_string = list(my_string)
print(my_string)