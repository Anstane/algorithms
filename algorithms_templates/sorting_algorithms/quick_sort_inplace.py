import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def partition(array, low, high):
    """Нахождение pivot`а.

    1) Берём переменную в виде минимального индекса;
    2) Опорный элемент = последний элемент массива;
    3) Проходим по числам в заданном диапазоне ->
    если искомое меньше pivot`а ->
    двигаем его влево;
    4) Доходя до крайнего элемента -> его также меняем местами.
    """
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    """Алгоритм быстрой сортировки.

    Получем pivot из partition -> рекурсивно делим на половины.
    """
    if len(array) == 1:
        return array
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)


if __name__ == '__main__':
    quick_sort(array, low=0, high=len(array) - 1)
    print(array)
