import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import sorted_random_array


array = sorted_random_array()
print(array)
goal = int(input())


def binary_search_recursion(array, goal, left, right):
    """Реализация бинарного поиска через рекурсию."""
    if left >= right:
        return -1
    mid = (left + right) // 2
    if array[mid] == goal:
        return mid
    elif goal > array[mid]:
        return binary_search_recursion(array, goal, mid + 1, right)
    else:
        return binary_search_recursion(array, goal, left, mid)


if __name__ == '__main__':
    print(binary_search_recursion(array, goal, left=0, right=len(array)))
