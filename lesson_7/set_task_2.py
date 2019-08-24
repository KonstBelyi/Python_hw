"""
Даны два списка чисел. Показать:
a) числа содержащиеся одновременно как в первом списке, так и во втором
b) числа содержащиеся в первом, но отсутствуют во втором
c) только уникальные числа для первого и второго списков.
"""

from random import randint

lst1 = [15, 4, 3, 9, 2, 8, 4, 20, 3, 6, 9, 7, 7]    #   [randint(1, 20) for _ in range(13)]
print('Список чисел #1: {}'.format(lst1))
lst2 = [7, 5, 14, 16, 18, 3, 10, 4, 20, 8]  #   [randint(1, 20) for _ in range(10)]
print('Список чисел #2: {}'.format(lst2))
lst1 = set(lst1)
lst2 = set(lst2)
print('a) числа содержащиеся одновременно как в первом списке, так и во втором: {}'.format(list(lst1.intersection(lst2))))
print('b) числа содержащиеся в первом, но отсутствуют во втором: {}'.format(list(lst1.difference(lst2))))
print('c) только уникальные числа для первого и второго списков: {}'.format(list(lst1.symmetric_difference(lst2))))
