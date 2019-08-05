print("Hello World!")
print('Hello \'World!\'')
print("Hello \"World!\"")
print('Hello \n"World\b"!')

'''

\a  - alert
\n  - new line
\b  - backspace
\'  
\"  
\\  
\t  - horizontal tab

'''

print("===================")
print(45)
print(34 + 5)
print("===================")
a = 12
b = 23
i = a + b
# print("Result of sum " + str(a) + " and " + str(b) + ":", i)
# print(i)
print("Result of sum {A} and {B}: {I}".format(B=b, I=i, A=a))
print("Result of sum {0} and {1}: {2}".format(a, b, i))
print("Result of sum {} and {}: {}".format(a, b, i))

print("===================")


print(len('Hello World!'))          # длина последовательности
print('Hello World!'.upper())       # верхний регистр
print('Hello World!'.lower())       # нижний регистр
print('Hello World!'[0])            # вывести нулевое значение в поледовательности
print('Hello World!'[6])            # вывести шестое значение в последовательности

'''
print('Hello World!'[start: stop: step])   -     выборка из последовательности 
                                                (start = начало выборки, stop - конец выборки, step = шаг выборки)
'''

print('Hello World!'[2:])           # начало выборки со второго значения
print('Hello World!'[6:11])         # выборка с 6го по 11е значение
print('Hello World!'[6:-1])         # выборка с первого значения с конца (где "!" - нулевое значение)
print('Hello World!'[6:-1:2])       # выборка каждого второго значения в заданом диапазоне с конца
print('Hello World!'[::-1])         # разворот диапазона значений
print('Hello World!'.find('l'))     # найти на каком месте находится первое значение "l"

idx = 'Hello World!'.find('l')          # найти первое значение "l" в последовательности
print(idx)
idx = 'Hello World!'.find('l', idx+1)   # найти где находится второе значение l
print(idx)
idx = 'Hello World!'.find('l', idx+1)   # найти где находится следующее значение l
print(idx)
print('==============================')
print(3**3)             # возведение в степень
print(int('25666'))     # преобразование в целое число
