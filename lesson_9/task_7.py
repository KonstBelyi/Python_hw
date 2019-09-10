"""
Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу
от -1 до 1, причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например,
последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]
"""

from random import randint

lst = [randint(-10, 10) for _ in range(10)]   # [6, -5, -2, 4, 0, -8, -6, -8, 0, 0]
print(lst)

if min(lst) * (-1) > max(lst):
    abs_maximum = min(lst)
else:
    abs_maximum = max(lst)

print('Абсолютный максимум данного списка: {}'.format(abs_maximum))

norm_list = []
element = lst[0]
for value in lst:
    element = round(value / abs_maximum, 2)
    if abs_maximum < 0:
        element *= (-1)
    if element == 0 or element == 1 or element == -1:
        element = int(element)
    norm_list.append(element)
print('Нормированный список: \n{}'.format(norm_list))
