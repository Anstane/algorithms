# Номер посылки - 86238315

from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Логика работы функции.

    1) Задаём переменные left и right;
    2) Создаём цикл while, который будет работать до тех пор,
    пока не будет найден target или right >= left;
    3) Ищем значение mid;
    4) Проверяем mid больше или меньше левой стороны,
    чтобы определить массив, в котором будем искать target;
    5) Реализуем стандратную логику бинарного поиска для массива,
    в котором находится наш target;
    6) Если не находим значение target в правом или левом массиве -
    возвращаем -1.
    """
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test() -> None:
    """Тестирование корректности работы алгоритма."""
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
