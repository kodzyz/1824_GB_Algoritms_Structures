# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# var_1
# [14, 5, 2, 14, 5, 11, 2, 3, 6, 3]
# 2 2
# var_2: быстрой сортировкой
# [3, 10, 9, 10, 10, 10, 5, 13, 4, 11]
# 3 4


print(f'var_1')
def mini(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    sub_min = min(arr[1:])
    return arr[0] if arr[0] < sub_min else sub_min


from random import random

N = 10
a = [0] * N
for _ in range(N):
    a[_] = int(random() * 15)

print(a)
print(mini(a), end=' ')
a.remove(mini(a))
print(mini(a))


print(f'var_2: быстрой сортировкой')


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        ref = arr[0]
        less = [i for i in arr[1:] if i < ref]
        greater = [i for i in arr[1:] if i > ref]
        return quicksort(less) + [ref] + quicksort(greater)


N = 10
b = [0] * N
for _ in range(N):
    b[_] = int(random() * 15)
print(b)
c = quicksort(b)
print(c[0], c[1])