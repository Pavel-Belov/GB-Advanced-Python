# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и знаменателем.
# Возвращает сумму и произведение дробей. Для проверки используется модуль fractions.

from fractions import Fraction


def res_frac(a, b):
    if a == b:
        return f'{a // b}'
    else:
        temp_a = a
        temp_b = b
        while temp_b:
            temp_a, temp_b = temp_b, temp_a % temp_b
        if b // temp_a == 1:
            return f'{a // temp_a}'
        else:
            return f'{a // temp_a}/{b // temp_a}'


frac_1 = input('Введите первую дробь вида вида "a/b": ').split('/')
frac_2 = input('Введите вторую дробь вида вида "a/b": ').split('/')

a_1 = int(frac_1[0])
b_1 = int(frac_1[1])
a_2 = int(frac_2[0])
b_2 = int(frac_2[1])

# сумма дробей
if b_1 != b_2:
    res_sum_b = b_1 * b_2
    res_sum_a = a_1 * b_2 + a_2 * b_1
else:
    res_sum_b = b_1
    res_sum_a = a_1 + a_2

# произведение дробей
res_mult_a = a_1 * a_2
res_mult_b = b_1 * b_2

# проверка модулем fractions
f1 = Fraction(a_1, b_1)
f2 = Fraction(a_2, b_2)
check_sum = f1 + f2
check_mult = f1 * f2

print(f'Сумма дробей: {res_frac(res_sum_a, res_sum_b)}\n'
      f'Произведение дробей: {res_frac(res_mult_a, res_mult_b)}\n'
      f'Проверка модулем fractions:\n'
      f'\tСумма: {check_sum}\n'
      f'\tПроизведение: {check_mult}')
