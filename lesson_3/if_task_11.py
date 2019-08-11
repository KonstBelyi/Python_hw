"""

Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
одним ходом.

"""
x1 = int(input('Please, enter the x1 position of the first cell (from 1 to 8): '))
y1 = int(input('Please, enter the y1 position of the first cell (from 1 to 8): '))
x2 = int(input('Please, enter the x2 position of the first cell (from 1 to 8): '))
y2 = int(input('Please, enter the y2 position of the first cell (from 1 to 8): '))
dx = x1 - x2
dy = y1 - y2
if dx < 0:
    dx *= -1
if dy < 0:
    dy *= -1
print(dx)
print(dy)
if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print('YES')
else:
    print('NO')
