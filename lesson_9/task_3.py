"""
Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из
моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло
между двумя моментами времени. Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый
момент времени и три целых числа, задающих второй момент времени. Выведите число секунд между этими моментами времени.
"""

hours_1 = int(input('Enter an hour for the first moment (0-23): '))
minutes_1 = int(input('Enter minutes for the first moment (0-59): '))
seconds_1 = int(input('Enter seconds for the first moment (0 - 59): '))
print()
hours_2 = int(input('Enter an hour for the second moment (0-23): '))
minutes_2 = int(input('Enter minutes for the second moment (0-59): '))
seconds_2 = int(input('Enter seconds for the second moment (0 - 59): '))

moment1_to_seconds = hours_1 * 360 + minutes_1 * 60 + seconds_1
moment2_to_seconds = hours_2 * 360 + minutes_2 * 60 + seconds_2
secs_between_moments = moment2_to_seconds - moment1_to_seconds
print()
print('Seconds between these two moments: {} seconds.'.format(secs_between_moments))
