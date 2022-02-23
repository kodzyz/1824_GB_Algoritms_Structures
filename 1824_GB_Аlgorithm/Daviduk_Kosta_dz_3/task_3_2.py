# 2. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

#example:
# [8, 9, 14, 8, 0]
# [8, 9, 0, 8, 14]


def smal_big(arr):
    mini = 0
    maxi = 0
    for i in range(len(arr)):
        if a[i] > a[maxi]:
            maxi = i
        elif a[i] < a[mini]:
            mini = i
    return maxi, mini


def swap(arr):
    maxi, mini = smal_big(arr)
    arr[maxi], arr[mini] = arr[mini], arr[maxi]
    return f'{arr}'


from random import random

N = 5
a = [0] * N
for _ in range(N):
    a[_] = int(random() * 15)

print(a)
print(swap(a))