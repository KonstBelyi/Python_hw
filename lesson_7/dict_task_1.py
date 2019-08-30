"""
В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в
этом тексте ранее. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним
или большим числом пробелов или символами конца строки.
"""
###
"""
пример строки:
чебурек подмышка кирогаз азбука карандаш если же не если то почему же и как от этого не хочу Но буду подмышка челюсть карандаш  подмышка
"""


counter = {}
string = input('Enter a string: ').split()
print(string)
for word in string:
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
# print()
# print('азбука:', counter['азбука'])
# print(counter)