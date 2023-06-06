# Задача 22
# from random import randint

# n = 20
# m = 15

# list_n = []
# list_m = []

# for i in range(n):
#     list_n.append(randint(0, 10))
# print(f'1-й набор: {list_n}')

# for i in range(m):
#     list_m.append(randint(0, 10))
# print(f'2-й набор: {list_m}')

# print(f'Пересечение: {sorted(list(set(list_n).intersection(set(list_m))))}')

# Задача 24 ягоды

# from random import randint

# berries = 1000
# bush_quantity = 10
# garden = []

# for i in range(bush_quantity):
#     garden.append(randint(0, berries))
# print(f'Исходная грядка {garden}')

# garden.append(garden[0])
# garden.append(garden[1])
# print(f'Грядка с добавленными в конец 1-м и 2-м кустами{garden}')

# sum = []
# maxsum = 0

# for i in range(1, len(garden)-1):
#     sum.append(garden[i - 1] + garden[i] + garden[i + 1])
#     if sum[i-1] > maxsum:
#         maxsum = sum[i-1]

# print(f'Суммы {sum}, ')
# print(f'За 1 заход, робот соберёт максимум {maxsum} ягод.')