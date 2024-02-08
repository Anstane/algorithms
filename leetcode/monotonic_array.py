from typing import List


def isMonotonic(A: List[int]) -> bool:
    # if nums == sorted(nums) or nums == sorted(nums, reverse=True):
    #     return True
    # return False

    # counter = 0
    # nums = set(nums)
    # nums = list(nums)
    # for i in range(len(nums) - 1):
    #     if nums[i] + 1 == nums[i + 1]:
    #         counter += 1
    #     if nums[i] - 1 == nums[i + 1]:
    #         counter -= 1
    # return counter == len(nums) - 1

    return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))

A = [1,3,2]
print(isMonotonic(A))