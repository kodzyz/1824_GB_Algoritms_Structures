#2 Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
# (Сделать без использования строк)

#per = input('Введите :  ')
per = '3486'


def reverse(a : str):
    l = []
    i = int(a)
    while i != 0:
        l.append(str(i % 10))
        i //= 10
    return f"reverse for {a} -> {''.join(l)}"

def reverse_1(a : str):
    nw = 0
    i = int(a)
    while i != 0:
        ntg = i % 10  # 6, 8, 4, 3
        i //= 10      # 348, 34, 3, 0
        nw *= 10      # 0, 60, 680, 6840
        nw += ntg     # 6, 68, 684, 6843
    return f"reverse for {a} -> {nw}"

b = reverse(per)
print(b)

b1 = reverse_1(per)
print(b1)