import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def find_minimum(array):
    """Функция для поиска минимального числа в массиве."""
    min_index = 0
    minimum = array[0]
    for i in range(1, len(array)):
        if minimum > array[i]:
            minimum = array[i]
            min_index = i
    return min_index


def selection_sort(array):
    """Алгоритм сортировки выбором."""
    new_array = []
    for i in range(len(array)):
        minimum = find_minimum(array)
        new_array.append(array[minimum])
        array.pop(minimum)
    return new_array


def selection_sort_inplace(array):
    """Алгоритм сортировки выбором без использованя доп. памяти."""
    for i in range(len(array)):
        minimum = find_minimum(array[i:])
        array[i + minimum], array[i] = array[i], array[i + minimum]
    return array


if __name__ == '__main__':
    print(selection_sort(array))
    print(selection_sort_inplace(array))
