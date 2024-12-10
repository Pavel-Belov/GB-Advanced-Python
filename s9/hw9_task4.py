# Задача 4. Кэширование для ускорения вычислений.
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами,
# возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция,
# и, если такие аргументы уже использовались, должен вернуть сохранённый результат
# вместо запуска расчёта.

from functools import cache


@cache
def fib(num: int):
    # print(f'Вычисление числа Фибоначчи для {num}')
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)


if __name__ == '__main__':
    print(fib(10))
    print(fib(20))
    print(fib(10))
