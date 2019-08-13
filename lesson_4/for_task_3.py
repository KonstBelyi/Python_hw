"""

Даны два целых числа `A` и `В`, `A > B`. Выведите все нечётные числа от `A` до `B` включительно, в порядке убывания.
В этой задаче можно обойтись без инструкции **if**.

"""
"""
# с инструкцией **if**
a = int(input('Enter number A: '))
b = int(input('Enter number B (B<A): '))
for i in range(a, b-1, -1):
     if i % 2 != 0:
         print(i)
"""

# Решение задачи (без использования **if**)
a = int(input('Enter number A: '))
b = int(input('Enter number B (B<A): '))
for i in range(a - (a + 1) % 2, b - b % 2, -2):     # каждое четное число в последовательности превращаем в нечетное и выводим получаемую последовательность с шагом "2"
    print(i)

"""
# для практики :) вывел четные числа
a = int(input('Enter number A: '))
b = int(input('Enter number B (B<A): '))
for i in range(a + a % 2, b - 1, -2):
    print(i)
"""