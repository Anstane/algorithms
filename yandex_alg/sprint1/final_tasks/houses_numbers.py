from typing import List


def distance_from_zero(n: int, houses_numbers: List[int]) -> str:
    zero = -n
    list_of_numbers = [0] * n

    for i in range(n):
        if houses_numbers[i]:
            list_of_numbers[i] = i - zero
        else:
            zero = i

    zero = 2 * n

    for i in reversed(range(n)):
        if houses_numbers[i]:
            list_of_numbers[i] = min(zero - i, list_of_numbers[i])
        else:
            zero = i

    return list_of_numbers

if __name__ == "__main__":
    n = int(input())
    houses_numbers = [int(numbers) for numbers in input().split()]
    print(*(distance_from_zero(n, houses_numbers)), sep=' ')
