from typing import List


def minOperations(nums: List[int], x: int) -> int:
    target = sum(nums) - x
    n = len(nums)

    if target == 0: # Если таргет сразу 0, тогда ответ - длина массива
        return n
    
    max_len = 0 # Длина массива - он же ответ
    current_sum = 0 # Текущая сумма
    left = 0 # Левый указатель - будет догонять right

    for right, value in enumerate(nums):
        current_sum += value # В текущую сумму запихиваем value right
        while current_sum > target and left <= right: # Когда cur > targer входим в цикл
            current_sum -= nums[left] # Отнимаем value left
            left += 1
        if current_sum == target: # Если находим cur == target
            max_len = max(max_len, right - left + 1) # Записываем это в max_len
    
    if max_len != 0: # Вычитаем записанный max_len из длины исходного массива
        return n - max_len # Столько нужно действий для нахождения ответа
    return -1
        