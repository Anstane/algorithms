array = [i for i in range(1, 10)]
len_num = [4, 3, 3, 6, 4, 5, 4, 6, 6]


def key_insert(key):
    """Ключ по которому происходит сортировка."""
    return len_num[key - 1]


def comparator(key_one, key_two):
    """Реализация с помощью компаратора."""
    return len_num[key_one - 1] < len_num[key_two - 1]


def insertion_sort(array, func):
    """Алгоритм сортировки вставками по ключу."""
    for i in range(len(array)):
        insert_item = array[i]
        j = i - 1
        while j >= 0 and func(insert_item) < func(array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = insert_item
        print(f'step {i}, sorted {i+1} elements: {array}')


if __name__ == '__main__':
    insertion_sort(array, key_insert)
