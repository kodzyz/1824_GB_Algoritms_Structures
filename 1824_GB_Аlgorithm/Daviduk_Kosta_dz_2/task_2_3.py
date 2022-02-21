# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

#per = input('Введите :  ')
per = '4'


def sum_row(amt: str):
    n = 1
    i = 0
    a = []
    sum = 0
    while len(a) < int(amt):
        a.append(n)
        sum += a[i]
        n *= -0.5
        i += 1
    return f"сумма {amt} элементов следующего ряда чисел: {''.join(str(a))}\nравна {sum}"


b = sum_row(per)
print(b)

