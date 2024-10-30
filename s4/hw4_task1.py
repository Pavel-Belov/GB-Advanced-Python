# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел,
# но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом:
# вывести сумму его цифр, максимальную или минимальную цифру.
# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

def digits_sum(num: int) -> int:
    res_sum = 0
    while num > 0:
        res_sum += num % 10
        num //= 10
    return res_sum


def max_digit(num: int) -> int:
    res_max = 0
    while num > 0:
        res_max = res_max if res_max > num % 10 else num % 10
        num //= 10
    return res_max


def min_digit(num: int) -> int:
    res_min = num % 10
    while num > 0:
        res_min = res_min if res_min < num % 10 else num % 10
        num //= 10
    return res_min


while True:
    result = 0
    number = int(input('Введите число: '))
    action = int(input('Выберите действие с числом:\n'
                       '1. Вывести сумму цифр числа\n'
                       '2. Вывести максимальную сумму числа\n'
                       '3. Вывести минимальную сумму числа\n'
                       '4. Закрыть калькулятор\n'))
    if action == 1:
        result = digits_sum(number)
    elif action == 2:
        result = max_digit(number)
    elif action == 3:
        result = min_digit(number)
    elif action == 4:
        break
    else:
        print('Введите номер операции из списка')
    print(f'Ответ: {result}')
