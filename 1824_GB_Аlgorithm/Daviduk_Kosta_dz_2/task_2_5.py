# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.


#amount = input('Number of input :  ')
#numb = input('number to be calculated :  ')

from random import randint

amount = '15'    # Количество вводимых чисел
numb = '1'  # цифра, которую необходимо посчитать
entered = [randint(1, 999) for i in range(int(amount))]  # последовательность чисел


def reiterative(like: str, arg_list: list):
    stor = 0
    for i in arg_list:
        while i > 0:
            if int(like) == i % 10:
                stor += 1
            i //= 10
    return f'"digit {like}" in sequences {arg_list} from "{amount}" input numbers\nmeets {stor} time'


b = reiterative(numb, entered)
print(b)


