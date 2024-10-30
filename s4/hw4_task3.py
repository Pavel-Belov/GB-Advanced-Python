# Задача 3. Число наоборот.
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит ответ на экран.
# Пример:
#     Введите первое число: 102
#     Введите второе число: 123
#     Первое число наоборот: 201
#     Второе число наоборот: 321
#     Сумма: 522
#     Сумма наоборот: 225

def num_reverse(number: int) -> int:
    count = 0
    digits = []
    reverse_number = 0

    while number > 0:
        digits.append(number % 10)
        number //= 10
        count += 1

    for n in digits:
        reverse_number += n * (10 ** (count - 1))
        count -= 1

    return reverse_number


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(f'Первое число наоборот: {num_reverse(num1)}')
print(f'Второе число наоборот: {num_reverse(num2)}')
print(f'Сумма: {num_reverse(num1) + num_reverse(num2)}')
print(f'Сумма наоборот: {num_reverse(num_reverse(num1) + num_reverse(num2))}')
