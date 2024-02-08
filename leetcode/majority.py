from typing import List
from collections import Counter


def majorityElement(nums: List[int]) -> List[int]:
    n = len(nums)
    amount_nums = Counter(nums)
    new_array = []

    for i in amount_nums:
        if amount_nums[i] > n / 3:
            new_array.append(i)
    
    if len(new_array) > 2:
        new_array = []

    return new_array


nums = [3,2,2,2,3]
print(majorityElement(nums))