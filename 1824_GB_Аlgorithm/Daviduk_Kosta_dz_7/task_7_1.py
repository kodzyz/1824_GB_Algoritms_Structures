# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.


import random


def quickselect_median(l, pivot_fn=random.choice):
    return quickselect(l, len(l) / 2, pivot_fn)


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):

        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


# m = 2
# l = [random.randint(-100, 100) for _ in range(2 * m + 1)]
# print(f'Исходный массив {l}')
# print(f'Медиана {quickselect_median(l)}')

l = [9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
print(quickselect_median(l))
