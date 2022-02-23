# 3. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

#example:
# a one dimensional array: [5, 8, 7, 8, 9, 0, 5, 10, 12, 10]
# between minimum and maximum elements: [5, 10]
# sum of elements: 15


def smal_big(arr):
    mini = 0
    maxi = 0
    for i in range(len(arr)):
        if a[i] > a[maxi]:
            maxi = i
        elif a[i] < a[mini]:
            mini = i
    return maxi, mini


def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def find_sum(arr):
    maxi, mini = smal_big(arr)
    if maxi > mini:
        print(f'between minimum and maximum elements: {arr[mini + 1:maxi:]}')
        return f'sum of elements: {sum(arr[mini + 1:maxi:])}'
    elif mini > maxi:
        print(f'between maximum and minimum elements: {arr[maxi + 1:mini:]}')
        return f'sum of elements: {sum(arr[maxi + 1:mini:])}'

from random import random

N = 10
a = [0] * N
for _ in range(N):
    a[_] = int(random() * 15)

print(f'a one dimensional array: {a}')

print(find_sum(a))