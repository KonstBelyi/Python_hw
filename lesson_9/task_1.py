"""
Написать следующие выражения:
(a + b * c)^2
a - 4 * b / c
(a * b + 4) / (c - 1)
"""

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))

print('Result for "(a + b * c) ^ 2" = "({A} + {B} * {C}) ^ 2" = ' .format(A=a, B=b, C=c) + str(int((a + b * c)**2)))
print('Result for "a - 4 * b / c" = "{A} - 4 * {B} / {C}" = ' .format(A=a, B=b, C=c) + str(int(a - 4 * b / c)))
print('Result for "(a * b + 4) / (c - 1)" = "({A} * {B} + 4) / ({C} - 1)" = ' .format(A=a, B=b, C=c) + str(int((a * b + 4) / (c - 1))))
