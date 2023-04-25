import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def insertion_sort(array):
    """Алгоритм сортировки вставками.

    1) Берём первое число и создаём изменяемую переменную;
    2) На первом шаге j = 0, поэтому условие цикла while не выполняется ->
    переходим к следующему;
    3) j = 1, если число слева меньше искомого, переходим к следующему ->
    в обратном случае ищем позицию для числа j;
    4) После нахождения позиции ->
    переходим к следующему числу.
    """
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')


if __name__ == '__main__':
    insertion_sort(array)
