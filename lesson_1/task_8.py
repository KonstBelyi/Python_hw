"""

Задание 8. Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке. (S = 1 / 2 * K1 * K2)

"""
print('=====================================')
a = 44
b = 35
print('Cathetus length K1 = {A} cm' .format(A=a))
print('Cathetus length K2 = {B} cm' .format(B=b))
c = 1/2
s = int(c * a * b)
print('Result of the area of a right triangle calculation is S = {C} * {A} * {B}, \nS = {S} cm^2'.format(A=a, B=b, C=c, S=s))
print('=====================================')
