# Задача 3. Проверка палиндрома.
# Напишите программу, которая принимает строку и определяет,
# является ли она палиндромом (читается одинаково с обеих сторон).

text = input('Введите строку: ').strip().lower()

refactor = ''.join([e for e in text if e.isalnum()])
res = 'Данная строка не является палиндромом'

if refactor == refactor[::-1]:
    res = 'Строка является палиндромом, она читается одинаково с обеих сторон'

print(res)
