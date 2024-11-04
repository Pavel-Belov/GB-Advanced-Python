# Задача 4. Генератор подстрок.
# Напишите генераторную функцию substrings(s), которая принимает строку s
# и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc На выходе будут выведены обозначения:
#     a
#     ab
#     abc
#     b
#     bc
#     c

def substrings(s: str):
    len_str = len(s)
    for ch1 in range(len_str):
        for ch2 in range(ch1 + 1, len_str + 1):
            yield s[ch1:ch2]


for substr in substrings('abc'):
    print(substr, end=' ')
