import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import random_array


array = random_array()
print(array)


def merge(array, left, mid, right):
    """Функция для склеивания левой и правой части."""
    left_arr = array[left:mid]
    right_arr = array[mid:right]

    result = []
    l, r = 0, 0

    while l != len(left_arr) and r != len(right_arr):
        if left_arr[l] <= right_arr[r]:
            result.append(left_arr[l])
            l += 1
        else:
            result.append(right_arr[r])
            r += 1

    result += left_arr[l:]
    result += right_arr[r:]

    array[left:right] = result

    return array


def merge_sort(array, left, right):
    """Сам алгоритм сортировки слиянием."""
    if left < right - 1:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid, right)
        merge(array, left, mid, right)
        return array


if __name__ == '__main__':
    print(merge_sort(array, left=0, right=len(array)))
