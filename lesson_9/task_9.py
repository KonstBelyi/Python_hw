"""
Дан список целых чисел, индекс k и значение C. Необходимо вставить в список на позицию с индексом k значение C, сдвинув
все элементы, имевшие индекс не менее k, вправо. Поскольку при этом количество элементов в списке увеличивается,
необходимо, перед сдвигом, увеличить список на один элемент, используя метод append().

Вставку необходимо осуществлять уже в расширеный списк, не создавая дополнительного списка.
Использовать метод insert() не разрешается.

Допустимо использовать append(), цикл, range() и оператор индексирования.
"""
from random import randint

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # [randint(0, 10) for _ in range(10)]
print('Исходный список: {}'.format(lst))
print()
k = int(input('Введите индекс k, куда вы хотите вставить новое число (от 0 до {}): '.format(len(lst)-1)))
C = int(input('Введите число C, которое вы хотите вставить по указанному индексу k = {}: '.format(k)))
print()

lst.append('x')

for i in range(-1, k - len(lst), -1):
    lst[i] = lst[i - 1]
    if lst[i] == lst[k]:
        lst[k] = C
print('Обновленный список: {}'.format(lst))