"""

Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
одним ходом.

"""

# посмотрел начало урока №4, похоже это еще один варинат решения этой задачи? :)

x1 = int(input('Please, enter the x1 position of the first cell (from 1 to 8): '))
y1 = int(input('Please, enter the y1 position of the first cell (from 1 to 8): '))
x2 = int(input('Please, enter the x2 position of the first cell (from 1 to 8): '))
y2 = int(input('Please, enter the y2 position of the first cell (from 1 to 8): '))
a = x1, y1
b = x2, y2
if b == (x1+1, y1+2):
    print('YES')
elif b == (x1+2, y1+1):
    print('YES')
elif b == (x1+2, y1-1):
    print('YES')
elif b == (x1+1, y1-2):
    print('YES')
elif b == (x1-1, y1-2):
    print('YES')
elif b == (x1-2, y1-1):
    print('YES')
elif b == (x1-2, y1+1):
    print('YES')
elif b == (x1-1, y1+2):
    print('YES')
else:
    print('NO')