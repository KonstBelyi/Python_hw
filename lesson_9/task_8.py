"""
Дан список. Необходимо его перевернуть. Использовать срезы, метод revers() и подобные встроенные механизмы, а так же
оператор IF ЗАПРЕЩЕНО. Можно использовать только цикл и арифметические операторы!
"""

lst = list('Hello World!')
print(lst)

j = -1
for i in range(len(lst)//2):
    lst[i], lst[j] = lst[j], lst[i]
    j -= 1
print(lst)
