# Задача 5. Яйца
# В рамках программы колонизации Марса компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте. Откладывать яйца
# слишком близко к поверхности опасно из-за радиации, а слишком глубоко — из-за давления грунта
# и недостатка кислорода. Вообще, факторов очень много, но специалисты проделали большую работу
# и предположили, что уровень опасности для черепашьих яиц рассчитывается по формуле:
#     D = x^3 − 3x^2 − 12x + 10,
#     где x — глубина кладки в метрах, а D — уровень опасности в условных единицах.
# Для тестирования гипотезы нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу, находящую такое значение глубины х, при котором уровень опасности как можно более
# близок к нулю. На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение х, удовлетворяющее этому отклонению.
# Известно, что глубина точно больше нуля и меньше четырёх метров. Обеспечьте контроль ввода.
#
# Пример:
#     Введите максимально допустимый уровень опасности: 0.01
#     Приблизительная глубина безопасной кладки: 0.732421875 м

MIN_OF_DEPTH = 0
MAX_OF_DEPTH = 4


def calculate_danger(depth):
    return depth ** 3 - 3 * (depth ** 2) - 12 * depth + 10


def calculate_depth(max_danger, min_depth, max_depth):
    middle_depth = (min_depth + max_depth) / 2
    middle_danger = calculate_danger(middle_depth)
    print(f'{middle_depth=:<30} {middle_danger=}')

    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            min_depth = middle_depth
        else:
            max_depth = middle_depth
        middle_depth = (min_depth + max_depth) / 2
        middle_danger = calculate_danger(middle_depth)
        print(f'{middle_depth=:<30} {middle_danger=}')

    return middle_depth


danger = float(input('Введите максимально допустимое отклонение уровня опасности от нуля: '))
if danger > 0:
    print(f'Допустимая глубина кладки равна {calculate_depth(danger, MIN_OF_DEPTH, MAX_OF_DEPTH)} м')
else:
    print('Ошибка ввода, допустимое отклонение должно быть больше нуля')