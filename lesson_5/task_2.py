"""

2. Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения
задачи метод `count`

"""

string = "Мама казала шо я хороший хлопчик"     # string = input('Please, enter a string:')
print('Our string: "{}"'.format(string))
print('Количество пробелов в строке: "{}"'.format(string.count(' ')))
print('Количество слов в строке: "{}"'.format(string.count(' ') + 1))
