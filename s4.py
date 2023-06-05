# Задача 25
# принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# import random
# my_list = [random.randint(0,10)for _ in range(20)]
# print(my_list)
# counter = {}
# for item in my_list:
#     counter[item] = counter.get(item, 0) + 1 # квадратные скобки ключ смена ключей
#     if counter.get(item) < 2:
#         print(item, end=' ')
#     else:
#         print(str(item) + '_' + str(counter.get(item)), end = ' '  )

#     print(item if counter.get(item) < 2 else str(item) + '_' + str(counter.get(item)), end = ' '  )
# print(my_dict.get(3, 0)



# st = input('ведите символы ')
# st = st.split()
# count_dict = {}
# for i in st:
#     if i in count_dict:
#         print(f'{i}_{count_dict[i]}', end = ' ')
#         count_dict[i] += 1
#     else:
#         print(i, end = ' ')
#         count_dict[i] = 1

# Задача 27
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# stroka = '''She sells  sea shells on the sea shore 
# The shells that she sells are sea shells 
# Im sure So if she sells sea
# shells on the sea shore  
# Im sure that the shells are sea
# shore shells'''

# from string import punctuation

# # for ch in ",.!": 
# for ch in punctuation: #убрать пунктуацию
#     stroka = stroka.replace(ch, '')
# stroka = stroka.lower().split()

# print(stroka)
# print(len(set(stroka)))


# stroka = stroka.lower() # нижний регистр
# stroka = stroka.split() # строка разделенная пробелами становится списком
# # stroka = stroka.lower().split()
# stroka = set(stroka)
# print(len(stroka))

# задача 29
# n = int(input())
# max_number = 1000
# while n != 0:
#     # n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)


# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 

# n = int(input("ведите число "))
# max_number = 0
# while n != 0 and n < 10:
#     n = int(input("ведите число "))
#     if max_number < n:
#         max_number = n
# print(max_number)