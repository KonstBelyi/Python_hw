"""

Задание 13. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то
же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть
не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт
чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из
трех классов.

"""

x1 = int(input('Students in class #1: '))
x2 = int(input('Students in class #2: '))
x3 = int(input('Students in class #3: '))
print('Sum of all students:', x1 + x2 + x3, '\b.')
print('Number of desks we need (one desk for each of two students) is:', round(((x1 + x2 + x3)/2) + 0.5))
