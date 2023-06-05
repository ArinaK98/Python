# Задача 25
# принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# print(str.split()) 

# stroka = input("Введите строку: ")
# my_list = list(stroka)

import random

my_list = input("Введите строку: ")
print(my_list)

counter = {}
for item in my_list:
    counter[item] = counter.get(item, 0) + 1

print(counter)
