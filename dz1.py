# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# n = int(input('введите трехзначное число '))
# a = (n//100)
# b = (n%10)
# с = ((n - (n//100*100))//10)
# print(a+b+с)

# n = int(input('введите трехзначное число '))
# print((n//100)+(n%10)+((n - (n//100*100))//10))


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# n = int(input('введите количество журавликов '))
# k = int(n/6*4)
# p = int(n/6)
# s = int(n/6)
# print(p, k, s)


# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = str(input('введите номер билета '))
# if ((n//100000)+((n%100000)//10000)+((n%10000)//1000)==((n%1000)//100)+((n%100)//10)+(n%10)):
#     print('билет счастливый!')
# else: print('билет не счастливый.')



# Задача 8: Требуется определить, можно ли от шоколадки
#  размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input('введите n '))
# m = int(input('введите m '))
# k = int(input('введите k '))
# if n==k or n*(m-1)==k:
#     print('yes')
# else: print('no')
# работает только для чисел из примера( 
# для больших чисел не получилось реализовать программу((