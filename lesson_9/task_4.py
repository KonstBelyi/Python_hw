"""
Определить является ли строка изограммой, т.е. что все буквы в ней за исключением пробелов встречаются только один раз.
Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами, а само слово 'изограмма' - нет.
"""

# string = 'Питон downstream книга без слов' # input('Please, enter a string: ')
# string = 'Питон downstream изограмма книга без слов'
string = 'Птон downstream кига без слв'

string = list(string)
print(string)

for value in string:
    if string.count(' ') > 0:
        string.remove(' ')
    if string.count(value) > 1:
        print('Строка не является изограммой!')
        break
else:
    print('Строка является изограммой!')
