# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(summa)

# sum_numbers(5)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
# # при return остановка

# # print(sum_numbers(5))
# a = sum_numbers(5)
# print(a)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
    

# print(sum_numbers(5))
# a = sum_numbers(5)
# print(a)

# Функции - сколько аргументов передаем, столько и принимаем
# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
    

# print(sum_numbers(5))
# a = sum_numbers(5, 'qweerty')
# print(a)

# если аргумент не передаем, то нужно задать его по умолчанию


# функция с неограниченным количеством аргументов - 
# необходимо использовать *

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'i'))
# print(sum_str('q', 'e', 'i', 'g'))
# print(sum_str(1,8,9))


# Импорт функции- импорт, обращение к импортируемому файлу, назание функции

# import modul1
# print(modul1. max1(5, 9))

# from modul1 import max1
# print(max1(10, 9))

# from modul1 import * 
# # импорт всех функций
# print(max1(10, 9))

# # импорт под другим названием
# import modul1 as m1
# print(m1.max1(10, 9))


#  рекурсия - необходимо указывать базис

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# алгоритмы

# Быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10,5,2]))

# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [1,2,5,3,7,4,8,0]
# merge_sort(list1)
# print(list1)