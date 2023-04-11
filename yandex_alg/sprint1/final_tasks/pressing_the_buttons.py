from typing import List
from collections import Counter


def counter(k: int, input_string: str) -> str:
    counter = 0
    numbers = Counter(input_string)
    for i in numbers.values():
        if i <= k:
            counter += 1

    return counter

if __name__ == "__main__":
    k = int(input()) * 2
    input_string = ''.join([input().replace('.', '') for i in range(4)])  
    print(counter(k, input_string))
