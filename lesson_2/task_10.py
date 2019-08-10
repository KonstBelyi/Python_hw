"""

Задание 10. Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные
часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.

"""
n = int(input('Please, enter the number of minutes: '))
h = int(n / 60)     # перевожу введеное количество минут в часы
print('Number of hours has passed after 0:00 : {} hour(s).'.format(h))
m = int(n % 60)     # получаю остаток минут
print('Number of minutes has passed after 0:00 : {} minute(s).'.format(m))
if h > 23:
    h = h - 24      # условие срабатывает, если количество часов > 23
if m < 10:
    m = '0' + str(m)
print('Time on watch, after {N} minutes has passed after 0:00 : {H}:{M}.'.format(N=n, H=h, M=m))
