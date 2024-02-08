from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    counter = 0
    # for i in range(len(nums)):
    #     for j in range(1, len(nums)):
    #         if nums[i] == nums[j] and i < j:
    #             counter += 1
    # return counter

    table = {}
    for val in nums:
        if val in table:
            counter += table[val]
            table[val] += 1
        else:
            table[val] = 1

    return counter

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))