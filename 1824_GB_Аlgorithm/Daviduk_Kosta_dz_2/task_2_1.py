#1 Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#Если в десятичной форме записи числа последняя цифра является чётной (0, 2, 4, 6 или 8),
# то всё число также является чётным, в противном случае — нечётным.

#per = input('Введите :  ')
per = '34560'


def even_odd_nums( a: int):
    num = a
    even_count = 0
    odd_count = 0
    d = []
    c = []
    i = 0
    while a != 0:
        if (a % 10 % 2) == 0:
            d.append(a % 10)
            even_count += 1
        else:
            c.append(a % 10)
            odd_count += 1
        a //= 10
        i += 1
    return f'for "{num}" number of even: {even_count} {d}, number of odd: {odd_count}{c}'


def even_odd_nums_1(a: str):
    even_count = 0
    odd_count = 0
    d = []
    c = []
    for i in a:
        if (int(i) % 2) == 0:
            d.append(int(i))
            even_count += 1
        else:
            c.append(int(i))
            odd_count += 1
    return f'for "{a}" number of even: {even_count} ({d}), number of odd: {odd_count}({c})'


def even_odd_nums_2(a: str):
    base_even = '02468'
    even_count = 0
    odd_count = 0
    d = []
    c = []
    for i in a:
        if i in base_even:
            d.append(int(i))
            even_count += 1
        else:
            c.append(int(i))
            odd_count += 1
    return f'for "{a}" number of even: {even_count} ({d}), number of odd: {odd_count}({c})'


b = even_odd_nums(int(per))
print(b)

b = even_odd_nums_1(per)
print(b)

b = even_odd_nums_2(per)
print(b)