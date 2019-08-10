"""

Задание 9. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа `n` и `k` и должна вывести искомое
количество яблок (два числа).

"""
n = int(input('Please, enter the number of students: '))
k = int(input('Please, enter the number of apples: '))
i = k // n
print('Number of apples for each student is: {I} apples.'.format(K=k, N=n, I=i))
x = k % n
print('Number of apples left in the basket: {} apples.'.format(x))
