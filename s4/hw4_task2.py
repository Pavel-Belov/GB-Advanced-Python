# Задача 2. Недоделка.
# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители.
# У предыдущего программиста было задание сделать две игры в одном приложении,
# чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли,
# перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит,
# победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор,
# пока он не отгадает загаданное.

import random


# Для упрощения ввода и лаконичности кода пусть пользователь вводит не строку, а цифру
def rock_paper_scissors() -> str:
    print('Игра «Камень, ножницы, бумага»')

    while True:
        pc = random.randint(1, 3)
        pc_choice = ''
        if pc == 1:
            pc_choice = 'камень'
        elif pc == 2:
            pc_choice = 'ножницы'
        elif pc == 3:
            pc_choice = 'бумагу'

        player = int(input('Выберите вариант: 1-камень, 2-ножницы, 3-бумага, 4-Выход\n'))

        if player == pc:
            print(f'Компьютер показал {pc_choice}. У вас ничья!')
        elif (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
            print(f'Компьютер показал {pc_choice}. Вы победили!')
        elif (player == 2 and pc == 1) or (player == 3 and pc == 2) or (player == 1 and pc == 3):
            print(f'Компьютер показал {pc_choice}. Вы проиграли!')
        elif player == 4:
            main_menu()
        else:
            print('Такого варианта нет, попробуйте ещё раз')


def guess_the_number():
    print('Игра «Угадай число»\nКомпьютер загадал число от 1 до 10')
    pc = random.randint(1, 10)

    while True:
        player = int(input('Введите число: '))

        if player < pc and 1 <= player <= 10:
            print('Загаданное число больше вашего. Попробуйте ещё раз.')
        elif player > pc and 1 <= player <= 10:
            print('Загаданное число меньше вашего. Попробуйте ещё раз.')
        elif player == pc:
            print('Угадали! Победа!')
            break
        else:
            print('Неверный ввод. Число должно быть от 1 до 10. Попробуйте ещё раз.')


def main_menu():
    while True:
        print('----------Главное меню----------\n'
              '1 - «Камень, ножницы, бумага»\n'
              '2 - «Угадай число»\n'
              '3 - Выйти\n'
              '--------------------------------')
        game = int(input('Выберите, во что вы хотите поиграть: '))

        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
        elif game == 3:
            print('До свидания! Заходите еще поиграть')
            break
        else:
            print('Ошибка выбора. Пожалуйста, введите один из представленных вариантов ещё раз!')


main_menu()
