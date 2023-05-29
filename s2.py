# объекты через подчеркивание 
# классы с больших букв

# while - цикл
# for - перебор

# Задача 1 факториал числа через цикл
# n = int(input('введите n '))
# i = 1
# factorial = 1
# while i <= n:
#     factorial = factorial * i
#     i += 1
# print(factorial)

# Задача 2 
number = int(input('введите  '))
i = 2
f_one = 0
f_two = 1
answer = f_one + f_two
while answer <= number:
    f_one = f_two
    f_two = answer
    answer = f_one + f_two
    i += 1
if number == answer:
    print(i)
print(-1)

