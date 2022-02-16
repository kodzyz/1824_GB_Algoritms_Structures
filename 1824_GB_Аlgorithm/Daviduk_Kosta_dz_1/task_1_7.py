# Задача 7
# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

#'4','5','6' -> треугольник существует и является разносторонним
#'4','7','7' -> треугольник существует и является равнобедренным
#'4','1','1' -> треугольника не существует
#'4','5','0' -> треугольника не существует

# n1 = int(input("Первый отрезок: "))
# n2 = int(input("Второй отрезок: "))
# n3 = int(input("Третий отрезок: "))
n1 = int('4')
n2 = int('7')
n3 = int('7')
#сумма длин любых его двух сторон больше третьей стороны
if n1 != 0 and n2 != 0 and n3 != 0 and (n1 + n2) > n3 and (n1 + n3) > n2 and (n3 + n2) > n1:
    print('треугольник существует')
    if n1 != n2 and n1 != n3 and n2 != n3:
        print('и является разносторонним')
    elif n1 == n2 == n3:
        print('и является равносторонним')
    else:
        print('и является равнобедренным')
else:
    print('треугольника не существует')