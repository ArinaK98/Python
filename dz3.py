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
# print(f'число {number} встречается в списке {my_list.count(number)} раз ')  )

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

# min_dist = float('inf')
# nearest = my_list[0]

# for i in my_list:
#     if abs(number - i) < min_dist:
#         min_dist = abs(number - i)
#         nearest = i

# print(f' Ближайшее число к { number} будет {nearest}')

# задача 
letters = {'AEIOULNSTRАВЕИНОРСТ' : 1, 'DGДКЛМПУ' : 2,
               'BCMPБГЁЬЯ' : 3, 'FHVWYЙЫ' : 4,'KЖЗХЦЧ' : 5,
                'XЭЮ' : 8,'QZЩЪ' : 10,}


word = input("Введите слово ")
total = 0
for ch in word.upper():
    for letter, score in letters.items():
        if ch in letter:
            total += score
print(f'слово {word} весит {total} очков ')


new_letters = {}
word = input("Введите слово ")

for key, value in letters.items():
    new_letters.update(dict.fromkeys(key, value))
total = 0
for ch in word.upper():
    total += new_letters.get(ch)
print(f'слово {word} весит {total} очков ')