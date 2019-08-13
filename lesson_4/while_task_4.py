"""

В первый день спортсмен пробежал `x` километров, а затем он каждый день увеличивал пробег на 10% от предыдущего
значения. По данному числу `y` определите номер дня, на который пробег спортсмена составит не менее `y` километров.
Программа получает на вход числа `x` и `y` и должна вывести одно число - номер дня.

"""

km_1_day = int(input('Enter the number of km on the first day: '))
km_N_day = int(input('Enter the number of km on the N day: '))
number_of_days = 0
while km_1_day <= km_N_day:
    km_1_day += km_1_day/10
    number_of_days += 1
print('Our runner wil run', km_N_day, 'km in', number_of_days, 'days.')
