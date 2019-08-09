"""

Длина маршрута велоралли "100 километров за 10 часов по Поясу Славы" - примерно 100 километров. Велосипедист Вася
стартует с нулевого километра маршрута и едет со скоростью `v` километров в час. На какой отметке он остановится через
`t` часов?

Программа получает на вход значение `v` и `t`. Если `v > 0`, то Вася движется в положительном направлении по маршруту,
если же значение `v < 0`, то в отрицательном.

Программа должна вывести целое число от 0 до 100 — номер отметки, на которой остановится Вася.

"""

v = float(input('Please, enter the cyclists speed (km/hr): '))
t = int(input('Please, enter in how many hours cyclist stops after start (hr): '))
if v < 0:
    v = -v
x = int(v * t)
if 0 <= x <= 100:
    print('The point, where cyclist stops after', t, 'hours from the start line, is:', x, 'kilometres.')
else:
    if x > 100:
        print('The cyclist is already relaxes on the beach ;)')
