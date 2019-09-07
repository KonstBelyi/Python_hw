"""
Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
"""
# Вариант 1
# number = list(input('Enter a 5-digits number, please: '))
#
# result = 1
# for i in range(len(number)):
#     if int(number[i]) % 2 != 0:
#         result *= int(number[i])
# print(result)

# Немного другой вариант
number = int(input('Enter a 5-digits number, please: '))
number = str(number)
result = 1
for i in range(len(number)):
    if int(number[i]) % 2 != 0:
        result *= int(number[i])
print(result)
