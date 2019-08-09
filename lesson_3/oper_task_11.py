"""

Дано трехзначное число. Найдите сумму его цифр.

"""

xyz = int(input('Enter a three-digit number: '))
x = xyz // 100
print('First digit in number', xyz, 'is:', x, '\b.')
y = (xyz // 10) % 10
print('Second digit in number', xyz, 'is:', y, '\b.')
z = xyz % 10
print('Third digit in number', xyz, 'is:', z, '\b.')
summ = x + y + z
print('The sum of all digits in number', xyz, 'is:', x, '+', y, '+', z, '=', summ, '\b.')
