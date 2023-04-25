from random import randint


def random_array():
    """Создаём массиив случайных чисел."""
    array = [randint(1, 100) for i in range(10)]
    return array


def sorted_random_array():
    """Создаём массив случайных числе в отсортированном виде."""
    array = [randint(1, 100) for i in range(10)]
    array.sort()
    return array
