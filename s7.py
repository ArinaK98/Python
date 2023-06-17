# функции высшего порядка 

#1. map

# my_list = list('123456789')
# print(my_list)

# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])
# print(my_list)

# my_list = list(map(int, my_list))
#  map ( что нам нужно получить(функцию), в отношении чего действовать(коллекция))
# не забыть завернуть в лист или объект в котором работаем


#2. filter - должнабыть функция содержащая тру фолс

# my_list = list(map(int, list('123456789')))
# def odd(num: int):
#     if num %2 == 0:
#         return True
#     return False

# even_list = list(filter(odd, my_list))
# print(even_list)


#3. enumerate

# my_list = list('saaf')

# for i in range(len(my_list)):
#     print(f'{i}. {my_list[i]}')

# for i, item in enumerate(my_list): #можно (my_list, число  )
#     print(f'{i+1}. {item}')

#4. zip объединение двух списков

# let_list = list('qwerty')
# num_list = list('123456')

# new_list = list(zip(let_list, num_list))
# print(new_list)

# если нужно склеить все элементы 
# from itertools import zip_longest + fillvalue = 'нету'

#5. lambda
# анонимная функция 

# def func(x,y):
#     return (x+y)

# func = lambda x,y: x+y
# print(func(3,4))


# my_list = '1234wefdf5678'
# new_list = list(filter(lambda x: x.isdigit(), my_list))
# print(new_list)

# my_list = []
# for i in range(10):
#     my_list.append(i)

# 6. листкомпрехейшн 
# my_list = [x for x in range(10)]
# print (my_list)

# my_list = [x for x in range(10) if x%2 ==0]
# print (my_list)

# my_list = [str(x) for x in range(10) if x%2 ==0]
# print (my_list)

# my_list = {str(x) for x in range(10) if x%2 ==0} # множество
# print (my_list)

# my_list = {str(x): x for x in range(10) if x%2 ==0} # кортеж 
# print (my_list)



# my_list = list(map(int, '1234578936542'))
# i = 0
# while True:
#     i += 1
#     if my_list[i]%2 == 0:
#         continue
#     print(my_list[i])

# continue - новая интерация не важно какие дальше действия





# Задача 49 
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. 
# Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. 

# from random import randint

# print(type_list := [((randint(1, 8)), randint(1, 8)) for _ in range(10)])
# type_list = list(filter(lambda x: x[0] != x[1],type_list))
# print(type_list := list(set(type_list)))
# print(new_list := list(map(lambda x: 3.14 * x[0]* x[1], type_list)))
# for i in type_list:
#     if i[0] * i[1] * 3.14 == max(new_list):
#         print(i, max(new_list))
#         break

# Задача 51
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):

# from typing import Callable

# def same_by(func: Callable, list_obj: list) -> bool:
#     result = []
#     for obj in list_obj:
#         result.append(func(obj))
#     if len(set(result)) == 1:
#         return True
#     return False

# print(same_by(lambda x: x % 2 == 0, [2,4,5,7,8]))

# функция считает количество гласных 

# 