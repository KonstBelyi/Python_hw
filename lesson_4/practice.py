# тут код с урока

"""
i = 1
while i <= 10:
    print(i ** 2)
    i += 1
"""

"""
n = int(input('Enter a number: '))
length = 0
while n > 0:
    n //= 10
    length += 1
print(length)
"""

"""
a = b = 1
while a != 0:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        print('Делить на 0 нельзя:', a)
        continue
    print(a / b)
"""

a = int(input('Введите целое число: '))
while a != 0:
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
    a = int(input('Введите целое число: '))
else:
    print('Ни одного отрицательного числа не встретилось')