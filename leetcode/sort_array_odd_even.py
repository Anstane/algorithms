from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    return sorted(nums, key=lambda x: x % 2)

nums = [3,1,2,4]
print(sortArrayByParity(nums))