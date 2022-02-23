# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

#example:
# multiple of "2" = 49 times
# multiple of "3" = 33 times
# multiple of "4" = 24 times
# multiple of "5" = 19 times
# multiple of "6" = 16 times
# multiple of "7" = 14 times
# multiple of "8" = 12 times
# multiple of "9" = 11 times

a = {}
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a.setdefault(j, [])
            a[j].append(i)

for key, val in a.items():
    print(f'multiple of "{key}" = {len(val)} times')