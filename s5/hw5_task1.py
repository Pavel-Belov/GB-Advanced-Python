# Задание 1. Квадраты чисел.
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите двумя способами: функция-генератор и генераторное выражение.

def squares_of_numbers(n: int):
    for num in range(1, n + 1):
        yield num ** 2


number = int(input('Введите целове число: '))
squares_of_nums = (i ** 2 for i in range(1, number + 1))

print('Последовательность из квадратов чисел от 1 до N:\n1. Функция-генератор')
for square in squares_of_numbers(number):
    print(square, end=' ')

print('\n2. Генераторное выражение:')
for square in squares_of_nums:
    print(square, end=' ')
