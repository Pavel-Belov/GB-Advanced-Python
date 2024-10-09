# Задача 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью символьной графики.
# Для вертикальных линий используйте символ вертикального штриха (|),
# а для горизонтальных — дефис (-). Пусть ширину и высоту рамки определяет пользователь.

WIDTH_SYMBOL = '-'
HEIGHT_SYMBOL = '|'
SPACE_SYMBOL = ' '

width = int(input('Введите ширину рамки: '))
height = int(input('Введите высоту рамки: '))

border = []
for i in range(height):
    border_string = HEIGHT_SYMBOL
    for _ in range(1, width - 1):
        if i == 0 or i == height - 1:
            border_string += WIDTH_SYMBOL
        else:
            border_string += SPACE_SYMBOL
    border_string += HEIGHT_SYMBOL
    border.append(border_string)

print(*border, sep='\n')
