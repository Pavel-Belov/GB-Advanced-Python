# Задача 2. Треугольник
# Треугольник существует только тогда,когда сумма любых двух его сторон больше третьей.
# Дано: a,b,c-стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка -
# стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы
# двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input('Введите сторону "a" треугольника: '))
b = float(input('Введите сторону "b" треугольника: '))
c = float(input('Введите сторону "c" треугольника: '))

s = f'Треугольника со сторонами {a}, {b}, {c} не существует'

if a + b > c and a + c > b and b + c > a:
    s = f'Треугольник со сторонами {a}, {b}, {c} существует и он является '
    if a == b == c:
        s += 'равносторонним'
    elif a == b != c or a == c != b or b == c != a:
        s += 'равнобедреннным'
    else:
        s += 'разносторонним'

print(s)
