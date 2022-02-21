# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# Дополнительно (рекурсивно):
# https://leetcode.com/problems/reverse-string/ https://leetcode.com/problems/power-of-two/


entered = []
ent = input('Sequence of numbers :  ')
entered.append(int(ent))
while int(ent) != 0:
    ent = input('Sequence of numbers :  ')
    entered.append(int(ent))
print(entered)

from random import randint

# amount = '5'    # Количество вводимых чисел
# entered = [randint(1, 999) for i in range(int(amount))]  # последовательность чисел


def larg_sum(arg_list: list):
    ma = 0
    for i in arg_list:
        th_num = i
        su = 0
        while i > 0:
            su += i % 10
            i //= 10
        if su > ma:
            ma = su
            num = th_num
    return f'in sequences {arg_list}\nlargest by sum of digits "{num}"\nthe sum of its digits = {ma}'


b = larg_sum(entered)
print(b)











