# Задача 5. Игра «Компьютер угадывает число»
# Мальчик загадывает число между 1 и 100 (включительно). Компьютер может спросить у мальчика:
# «Твоё число равно, меньше или больше, чем число N?», где N —число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

ANSWER_TEXT = '1 - равно, 2 - больше, 3 - меньше: '

lower_limit = 1
upper_limit = 100
count = 1
print('Загадайте число от 1 до 100, а компьютер попытается отгадать его за семь ходов')

while True:
    num = (lower_limit + upper_limit) // 2
    print(f'Загаданное число равно, больше или меньше {num}?')
    answer = int(input(ANSWER_TEXT))

    if answer == 1:
        print(f'Загаданное число - {num}. Угадано за {count} попыток')
        break
    elif answer == 2:
        lower_limit = num
    elif answer == 3:
        upper_limit = num

    count += 1