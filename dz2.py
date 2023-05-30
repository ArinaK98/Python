# Задача 10

# n = int(input('введите количество монет '))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input('введите 0-решка 1- орел'))
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# Задача 12

# s = int(input('введите сумму '))
# p = int(input('введите произведение '))
# for i in range(s):
#     for j in range(p):
#         if s == i + j and p == i * j:
#             print(i, j)

# # Задача 14

# n = int(input('введите число n'))
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1