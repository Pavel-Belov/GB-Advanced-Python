# Задание 2. Преобразование числа в шестнадцатеричное представление
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input('Введите число: '))

hex_symbols = '0123456789abcdef'
hex_check = hex(number)
hex_string = ''
hex_negative = ''

if number == 0:
    hex_string = '0x0'

else:
    if number < 0:
        hex_negative = '-'
        number *= -1

    while number > 0:
        hex_index = number % 16
        hex_string = hex_symbols[hex_index] + hex_string
        number //= 16

    hex_string = hex_negative + '0x' + hex_string

print(f'Шестнадцатеричное представление: {hex_string}\n'
      f'Проверка функцией hex: {hex_check}')
