import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def quick_sort(array):
    """Алгоритм быстрой сортироки.

    Ищем опорный элемент -> делим на лево и право -> рекурсивно склеиваем.
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        low = [i for i in array[1:] if pivot >= i]
        high = [i for i in array[1:] if pivot < i]
        return quick_sort(low) + [pivot] + quick_sort(high)


if __name__ == '__main__':
    print(quick_sort(array))
