"""

Задание 10. Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные
часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.

"""
print('===========================')
n = 1856
print('Number of minutes after 0 AM: {} minutes.'.format(n))
k = 60
h = int(n / k)
print('Number of hours has passed after 0 AM: {}.'.format(h))
m = int(n % k)
print('Number of minutes left: {}.'.format(m))
x = h - 24
print('Time on watch, after {N} minutes has passed after 0 AM: {X}:{M}.'.format(N=n, X=x, M=m))
