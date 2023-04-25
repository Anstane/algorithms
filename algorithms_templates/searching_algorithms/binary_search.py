import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import sorted_random_array


array = sorted_random_array()
print(array)
goal = int(input())


def binary_search(array, goal):
    """Алгоритм бинарного поиска."""
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if goal > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return mid

if __name__ == '__main__':
    print(binary_search(array, goal))
