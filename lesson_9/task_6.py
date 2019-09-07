"""
В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
Новый список создавать нельзя!
"""

from random import randint

lst = [randint(1, 20) for _ in range(10)]  # [16, 16, 5, 15, 3, 9, 12, 6, 16, 19]
print(lst)

for element in lst:
    if element == lst[lst.index(min(lst))]:
        element = lst[lst.index(max(lst))]
    elif element == lst[lst.index(max(lst))]:
        element = lst[lst.index(min(lst))]
    print(element, end=', ')

