# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

#per = input('Введите :  ')
per = '10'


def equa_check(amt: str):
    n = int(amt)
    s_m = 0
    a = []
    for i in range(1, n+1, 1):
        a.append(i)
        s_m += a[len(a)-1]
    if s_m == n*(n+1)/2:
        return f" при 'n = {n}' выполняется равенство {''.join(str(a)).replace(',', ' +')} = n(n+1)/2 = {s_m}"
    else:
        return f'False'


b = equa_check(per)
print(b)

