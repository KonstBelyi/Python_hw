"""

Дана строка, в которой буква `h` встречается минимум два раза. Удалите из этой строки первое и последнее вхождение
буквы `h`, а также все символы, находящиеся между ними.

При решении этой задачи использовать циклы - ЗАПРЕЩЕНО! (Задача решается в 3 (три) строчки кода. Понадобятся методы поиска,
срезы и метод replace)

"""

string = 'Manhattan is my home for this hard year!'
print(string)
first_h = string.find('h')
print('The index of the first "h" is: {}'.format(first_h))
last_h = string.rfind('h')
print('The index of the last "h" is: {}'.format(last_h))
string = string.replace(string[first_h:last_h+1], '')
print(string)
