# def get_2_x_2():
#     print(2 * 2)
#
# get_2_x_2()
# print(get_2_x_2())

# def draw_rect():
#     for _ in range(11):
#         for _ in range(11):
#             print('*', end='  ')
#         print()
#
# draw_rect()

# def draw_triangle():
#     h = 15
#     for i in range(h):
#         for j in range(h - i):
#             print(' ', end='')
#         for j in range(h - 2 * i, h + 1):
#             print('*', end='')
#         print()
#
# draw_triangle()

# def func(x):
#     print('param x =', x)
#     x = 3
#     print('local x =', x)
#
#
# a = 4
# print('before func a =', a)
# func(a)
# print('after func a =', a)

# def func_outer():
#     x = 2
#     print('x equal:', x)
#
#     def func_inner():
#         nonlocal x
#         x = 5
#
#     func_inner()
#     print('Local variable \'x\' change to:', x)
#
#
# func_outer()

# def multi_var(*args):
#     print(args)
#     for value in args:
#         print(value, end=', ')
#     print()
#
# multi_var(1, 2, 3, 'ads')
#
# a = 5
# b = 9
# c = 2
#
# multi_var(a, 4+5, 'Hello World!', b, c)

# def multi_kw(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print('key = {k:12}\tvalue = {v}'.format(k=key, v=value))
#     print()
#
#
# multi_kw(name='Ivan', job='Worker', salary=5600)
#
# multi_kw(type='lorry', model='IVECO', length=25.7, weight=8500)

# def list_compare(a, b):
#     if a > b:
#         return 1
#     elif a < b:
#         return -1
#     else:
#         return 0
#
#
# def dict_compare(a, b):
#     if len(str(list(a.values())[0])) > len(str(list(b.values())[0])):
#         return 1
#     elif len(str(list(a.values())[0])) < len(str(list(b.values())[0])):
#         return -1
#     else:
#         return 0
#
#
# def comparing(collection, comparator):
#     i = iter(collection)
#     try:
#         while True:
#             d1 = next(i)
#             d2 = next(i)
#             if comparator(d1, d2) == 0:
#                 print(f'{d1} == {d2}')
#             else:
#                 print(f'{d1} <> {d2}')
#     except StopIteration as ex:
#         print('End of collection')
#
#
# lst = [2, 5, 3, 3, 4, 3, 3, 2, 1, 1]
# dic = [{'type': 'lorry'}, {'model': 'IVECO'}, {'length': 25.7}, {'weight': 8500.1}]
#
# comparing(lst, list_compare)
#
# comparing(dic, dict_compare)

def fahrenheit(T):
    return round(((float(9)/5)*T + 32), 2)


def celsius(T):
    return round((float(5)/9)*(T-32), 2)


temperatures = (36.5, 37, 37.5, 38, 39)
print(type(temperatures))
F = map(fahrenheit, temperatures)
C = map(celsius, F)

temperatures_in_fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_celsius = list(map(celsius, temperatures_in_fahrenheit))
print(temperatures_in_fahrenheit)
print(temperatures_in_celsius)
