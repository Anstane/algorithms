array = [0, 2, 1, 2, 0, 0, 1]


def counting_sort(array):
    """Сортировка подсчётом.

    Данная сортировка используется только,
    когда известно максимальное значение в исходном массиве.
    """
    new_array = [0] * 3

    for num in array:
        new_array[num] += 1

    result = [num for num, count in enumerate(new_array) for i in range(count)]
    return result


if __name__ == '__main__':
    print(counting_sort(array))
