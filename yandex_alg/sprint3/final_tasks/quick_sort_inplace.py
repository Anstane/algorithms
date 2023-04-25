# Номер посылки - 86238302

from typing import List, NamedTuple


class Members(NamedTuple):
    """Класс содержит информацию об участнике."""

    score: int
    penalty: int
    name: str


def read_input() -> List[Members]:
    """Импортируем данные и приводим их в корректный вид."""
    number_of_members = int(input())
    participants = [input().split() for _ in range(number_of_members)]
    members = [
        Members(-int(score), int(penalty), name)
        for name, score, penalty in participants
    ]
    return members


def partition(array: List[Members], low: int, high: int) -> int:
    """Вспомогательная функция для q_sort.

    1) Выбираем последний элемент pivot`ом;
    2) Элементы, которые меньше pivot`а двигаются влево, больше - вправо.
    3) Возвращаем индекс нашего pivot`а.
    """
    left_index = low - 1
    pivot = array[high]

    for low_num in range(low, high):
        if array[low_num] <= pivot:
            left_index += 1
            (
                array[left_index], array[low_num]
            ) = (
                array[low_num], array[left_index]
            )

    array[left_index + 1], array[high] = array[high], array[left_index + 1]
    return left_index + 1


def q_sort(array: List[Members], low: int, high: int) -> None:
    """Функция рекурсивно сортирует значения.

    Сортировка относительно pivot`а,
    полученного с помощью функции partition.
    """
    if len(array) == 1:
        return array
    elif low < high:
        pivot = partition(array, low, high)
        q_sort(array, low, pivot - 1)
        q_sort(array, pivot + 1, high)


if __name__ == '__main__':
    members = read_input()
    q_sort(members, low=0, high=len(members) - 1)
    [print(member.name) for member in members]
