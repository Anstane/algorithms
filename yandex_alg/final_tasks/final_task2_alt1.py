from typing import Tuple, List
from collections import Counter

def counter(k: int, array: List[int]) -> int:
    counter = 0
    numbers = Counter(array)
    for i in numbers.values():
        if i <= k:
            counter += 1

    if array == None:
        counter = 0

    return counter

"""Читаем input и перобразуем в необходимый формат."""
def read_input() -> Tuple[int, List[int]]:
    k = int(input()) * 2
    list_of_numbers = [' '.join(input().replace('.', '')) for i in range(4)]
    array = []
    for j in list_of_numbers:
        array.extend(j.split(' '))

    try:
        if array == ['', '', '', '']:
            array = None
        else:
            array = list(map(int, array))
    finally:
        return k, array

    # Если ключ не . - тогда можно обрабатывать

k, array = read_input()

if __name__ == "__main__":
    print(counter(k, array))
