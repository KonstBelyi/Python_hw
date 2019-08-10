"""

Дано положительное действительное (вещественное) число `X`, которое имеет два знака после десятичной точки.
    - Выведите его дробную часть.
    - Выведите его первую цифру после десятичной точки.

"""
x = float(input('Please, enter a number with two digits after the decimal point: '))
y = x % int(x)      # берем дробную часть
print('The fractional part of the number {} is: {}.'.format(x, y))
z = int(y * 10)     # получаем первую цыфру после десятичной точки
print('The first digit after the decimal point is: {}.'.format(z))
