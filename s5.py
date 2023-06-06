# Рекурсия

# Задача 31
# Последовательностью Фибоначчи называется последовательность 
# чисел. Требуется найти N-е число Фибоначчи. Рекурсия.


# n = int(input('Введите число n: '))

# def fib(n):
#     if n in [1,2]:
#         return 1
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
#     return fib(n-1) + fib(n-2)

# print(fib(n))


# Задача 33 максимальный элементы заменить на минимальные
   
# from random import randint

# mark = []
# lens = int(input("введите длину списка:"))
# for i in range(lens):
#     mark.append(randint(1, 5))
# print(mark)
# maximal = max(mark)
# minimal = min(mark)
# for i in range(len(mark)):
#     if mark[i] == maximal:
#         mark[i] = minimal
# print(mark)

# задача 35 является ли число простым

# def simple_number(num):
#     kol = 0
#     for i in range(1, num + 1):
#         if num % 1 == 0:
#             kol += 1
#         if kol == 2:
#             return(f"Число {num} простое")
#         else:
#             return(f"Число {num} составное")

# print(simple_number(17))

# def is_simple(number: int) -> bool:
#     if number in [1,2]:
#         return True
#     if number % 2 == 0:
#         return False
#     for dev in range(3, number//2 + 1,2):
#         if number % dev == 0:
#             return False
#     return True
        
# print(is_simple(17))

# задача 37
# последовательность в обратном порядке.
# без массива и цикла



# def return_numbers(length):
#     if length == 0:
#         return " "
#     numbers = input("ведите число ")
#     return return_numbers(length - 1) + numbers + " "
# print(return_numbers(4))    
    

