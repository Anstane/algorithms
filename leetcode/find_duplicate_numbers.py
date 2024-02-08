from typing import List


def findDuplicate(nums: List[int]) -> int:
    nums_dict = {}
    for i, val in enumerate(nums): # Задачи почти аналог two sum
        if val in nums_dict:
            return val
        nums_dict[val] = i


nums = [1,3,4,2,2]
print(findDuplicate(nums))
