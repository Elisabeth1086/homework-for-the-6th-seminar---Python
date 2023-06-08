# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

n = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(n)
m = []
max = int(input('Введите максимальное число: '))
min = int(input('Введите минимальное число: '))

for i in range(len(n)):
    if n[i] >= min and n[i] <= max:
        m.append(i)
        print(m)
# или
# for i in range(len(n)):
#     if min <= n[i] <= max:
#         print(i, end=' ')