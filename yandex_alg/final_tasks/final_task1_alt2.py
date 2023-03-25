from typing import List

def zero_or_one(n: int, houses_numbers: List[int]) -> List[int]:
    list_of_numbers = [n] * n
    list_of_numbers2 = [n] * n


    for i, value in enumerate(houses_numbers):

        if value == 0:
            list_of_numbers[i] = 0
        else:
            list_of_numbers[i] = list_of_numbers[i - 1] + 1


    for i, value in enumerate(houses_numbers[::-1]):

        if value == 0:
            list_of_numbers2[i] = 0
        else:
            list_of_numbers2[i] = list_of_numbers2[i - 1] + 1


    return ' '.join(map(str, (map(min, zip(list_of_numbers, reversed(list_of_numbers2))))))      


def import_input() -> List[int]:

    with open('input.txt', 'r') as input:
        n = int(input.readline())
        houses_numbers = [
            int(numbers) for numbers in input.readline().split()
        ]

    return n, houses_numbers

n, houses_numbers = import_input()

if __name__ == "__main__":
    with open('output.txt', 'w') as output:
        output.write(zero_or_one(n, houses_numbers))
