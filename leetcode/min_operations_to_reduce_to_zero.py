from typing import List


def minOperations(nums: List[int], x: int) -> int:
    target = sum(nums) - x # (1 + 1 + 4 + 2 + 3) - 5 = 6
    n = len(nums)

    if target == 0: # Если 0 - длина массива ответ
        return n
    
    max_len = 0 # Длина массива - он же ответ
    current_sum = 0 # Текущая сумма
    left = 0 # Левый указатель - будет догонять right

    for right, value in enumerate(nums):
        current_sum += value # В текущую сумму запихиваем value right (+ 1 + 1 + 4 + 2 = 8)
        while current_sum > target and left <= right: # Когда cur > target входим в цикл
            current_sum -= nums[left] # Отнимаем value left (8 - 1 - 1)
            left += 1 (1, 1)
        if current_sum == target: # Если находим cur == target
            max_len = max(max_len, right - left + 1) # Записываем это в max_len
    
    if max_len != 0: # Вычитаем записанный max_len из длины исходного массива
        return n - max_len # Столько нужно действий для нахождения ответа
    return -1


nums = [1,1,4,2,3]
x = 5
print(minOperations(nums, x))
