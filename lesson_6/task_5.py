"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),
и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
поскольку у них недостаточно соседей.
"""

# # Вариант 1
# from random import randint
#
# lst = [randint(1, 20) for _ in range(20)]
# print('Our list:', lst)
# summ = 0
# for idx in range(1, len(lst) - 1):
#     if lst[idx] > lst[idx - 1] and lst[idx] > lst[idx + 1]:
#         summ += 1
# print('Number of Greatest Neighbours: "{}".'.format(summ))


# # Вариант 2
from random import randint

lst = [randint(1, 20) for _ in range(20)]
print('Our list:', lst)
print('Number of Greatest Neighbours: "{}".'.format(len([element for idx, element in enumerate(lst[1:-1]) if element > lst[idx] and element > lst[idx + 2]])))
