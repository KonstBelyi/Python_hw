"""

В математике функция `sign(x)` (знак числа) определена так:
    ``
    sign(x) = 1, если x > 0,
    sign(x) = -1, если x < 0,
    sign(x) = 0, если x = 0.
    ``

    Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных
    инструкций if... elif... else.

"""

x = int(input('Please, enter a number: '))
if x > 0:
    print('The sign(x) value for the number {} is: 1.'.format(x))
elif x < 0:
    print('The sign(x) value for the number {} is: -1.'.format(x))
else:
    print('The sign(x) value for the number {} is: 0.'.format(x))
