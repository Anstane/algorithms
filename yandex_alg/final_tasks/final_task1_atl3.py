# Номер посылки - 84388697

from typing import List


"""
Измеряем дистанцию от ближайшего нуля с двух концов
и выводим меньший показатель.
"""
def distance_from_zero(houses_numbers: List[int]) -> str:
    n = len(houses_numbers)
    zero = -n # Предварительно ставим 0 последним числом
    list_of_numbers = [0] * n # Создаём список из 0 в диапозоне n

    # Двигаемся слева направо высчитывая расстояние от последнего нуля
    for i in range(n):
        if houses_numbers[i]:
            list_of_numbers[i] = i - zero
        else:
            zero = i

    zero = 2 * n # Предварительно ставим 0 в обртаный конец списка

    # Двигаемся справа налево
    for i in reversed(range(n)):
        if houses_numbers[i]:
            list_of_numbers[i] = min(zero - i, list_of_numbers[i])
        else:
            zero = i

    return list_of_numbers

# """С помощью контекстного менеджера получаем input."""
# def import_input() -> List[int]:
#     with open('input.txt', 'r') as input:
#         n = int(input.readline())
#         houses_numbers = [
#             int(numbers) for numbers in input.readline().split()
#         ]
#     return houses_numbers

if __name__ == "__main__":

    n = int(input())
    houses_numbers = [int(numbers) for numbers in input().split()]
    print(*(distance_from_zero(houses_numbers)), sep=' ')
    # with open('output.txt', 'w') as output:
    #     output.write(distance_from_zero(import_input()))
