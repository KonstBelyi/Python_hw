"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).

Небольшая подсказка. В этой задаче вам понадобится, список, метод revers() (или срез [::-1]), чтоб развернуть список,
метод join() и строка ascii_uppercase из модуля string (её можно получить если сделать импорт
from string import ascii_uppercase), она содержит все буквы латинского алфавита.
"""

import string


def converter():
    symbols = list(string.digits + string.ascii_uppercase)

    number = int(input('Enter a number: '))
    system = int(input('Enter a system you want to convert in (2 - 36): '))

    symbols = symbols[0:system]

    element = ''
    while number > 0:
        element = str(number % system) + ' ' + element
        number //= system

    element = element.split()

    for i in range(len(element)):
        element[i] = symbols[int(element[i])]
    print('The new number in a chosen system is: {}.' .format(''.join(element)))


converter()
