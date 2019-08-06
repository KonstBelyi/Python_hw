"""

Задание 9. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа `n` и `k` и должна вывести искомое
количество яблок (два числа).

"""
print('===================================')
n = 15
print('Number of students n = {N}'.format(N=n))
k = 68
print('Number of apples k = {K}'.format(K=k))
i = k // n
print('Number of apples for each student is: {K}/{N} = {I} apples'.format(K=k, N=n, I=i))
x = k % n
print('Number of apples left in the basket: {}'.format(x))
