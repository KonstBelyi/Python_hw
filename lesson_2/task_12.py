"""

Задание 12. Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере
(пробелы важны!). Первая строка содержит следующее значение, а втора строка содержит предыдущее значение введёного
числа

    ```
        Please enter an integer number: 1234
        The next number for the number 1234 is 1235.
        The previous number for the number 1234 is 1233.

     or

        Please enter an integer number: 0
        The next number for the number 0 is 1.
        The previous number for the number 0 is -1.

"""

n = int(input('\tPlease enter an integer number: '))
print('\tThe next number for the number', n, 'is', n+1, '\b.')
print('\tThe previous number for the number', n, 'is', n-1, '\b.')
print('\n or \n')
n = int(input('\tPlease enter an integer number: '))
print('\tThe next number for the number', n, 'is', n+1, '\b.')
print('\tThe previous number for the number', n, 'is', n-1, '\b.')
