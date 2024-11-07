# Задание 1. Модуль для подсчета количества повторений слов.
# Создайте модуль с функцией, которая получает список слов и возвращает словарь,
# в котором ключи — это слова, а значения — количество их повторений в списке.

from word_count import count_word_occurrences

data = ['apple', 'banana', 'apple', 'orange']
print(count_word_occurrences(data))
