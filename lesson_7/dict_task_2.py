"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите все,
которые подходять по условию задачи. Задачу необходимо решить с использованием словаря.
"""

"""
текст для примера:
one two three three five six eight three two two five three
"""

dic = {}
text = input('Enter a text: ').split()
print(text)
for word in text:
    dic[word] = dic.get(word, 0) + 1
for freq_word, value in dic.items():
    if value == max(dic.values()):
        print('The most frequent word is:', freq_word)
