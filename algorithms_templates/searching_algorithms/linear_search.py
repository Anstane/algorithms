import sys
sys.path.append('algorithms_templates/..')
from algorithms_templates.core import sorted_random_array


array = sorted_random_array()
print(array)
goal = int(input())


def linear_search(array, goal):
    """Алгоритм линейного поиска - O(n)."""
    for i in range(len(array)):
        if array[i] == goal:
            return i
    return -1


if __name__ == '__main__':
    print(linear_search(array, goal))
