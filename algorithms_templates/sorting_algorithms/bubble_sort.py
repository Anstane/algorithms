import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def bubble_sort(array):
    """Сортировка пузырьком.

    Логика работы сортировки:
    1) Берём диапозон чисел len(array) - 1;
    2) Перебираем числа в этом диапозоне сравнивая их друг с другом;
    3) Если левое число больше правого -> меняем их местами.
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == '__main__':
    print(bubble_sort(array))
