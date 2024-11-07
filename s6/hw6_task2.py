# Задача2. Модуль для удаления дублирующихся подряд символов.
# Напишите модуль с функцией, которая принимает строку и возвращает строку
# с удаленными дублирующимися подряд идущими символами.
# Например, строка "aabbccaa" должна быть преобразована в "abca".

from remove_duplicates import remove_consecutive_duplicates

input_string = 'aaabbcaaa'
print(remove_consecutive_duplicates(input_string))
