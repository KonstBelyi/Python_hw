"""
Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов. Необходимо развеннуть
словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве
ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.

apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa
"""

eng_to_latin = {
    'apple': 'malum, pomum, popula',
    'fruit': 'baca, bacca, popum',
    'punishment': 'malum, multa',
}
print(eng_to_latin)
print(eng_to_latin.items())
print(list(eng_to_latin.items()))


for i in eng_to_latin.items():
