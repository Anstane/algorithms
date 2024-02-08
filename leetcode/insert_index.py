from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target == 0:
        return 0

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))
