# Задача 5. Нахождение анаграмм.
# Напишите программу, которая принимает два слова
# и определяет, являются ли они анаграммами.

def get_char_dict(word):
    res_dict = {}
    for char in word:
        res_dict[char] = res_dict.get(char, 0) + 1
    return res_dict


word_1 = input('Введите первое слово: ').lower()
word_2 = input('Введите второе слово: ').lower()
d_1 = get_char_dict(word_1)
d_2 = get_char_dict(word_2)

if len(word_1) != len(word_2) or d_1 != d_2:
    res = 'Слова не являются анаграммами'
else:
    res = 'Слова являются анаграммами'

print(res)
