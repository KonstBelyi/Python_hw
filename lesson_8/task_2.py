"""
2.	Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига,
второй параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр
задаёт направление сдвига (по умолчанию влево (False)).
"""

number = '123456789'
print('Исходное число =', number)
number = list(number)

def sdvig():
    sdvig_number = input('Введите число для сдвига: ')
    steps = int(input('Введите количество разрядов для сдвига: '))
    direction = input('Введите True, чтобы сдвинуть число вправо, или False, чтобы сдвинуть его влево: ')
    sdvig_number_idx = number.index(sdvig_number)
    del number[sdvig_number_idx]
    if direction == 'True':
        number.insert(sdvig_number_idx + steps, str(sdvig_number))
    if direction == 'False':
        number.insert(sdvig_number_idx - steps, str(sdvig_number))
    print('Число на выходе: ')
    for i in range(len(number)):
        print(number[i], end='')

sdvig()
