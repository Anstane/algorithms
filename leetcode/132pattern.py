from typing import List

# Given an array of n integers nums, a 132 pattern is a subsequence of three integers
# nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].



def find132pattern(nums: List[int]) -> bool:
    # table = {}

    # for i, val in enumerate(nums): # {0: 3, 1: 1, 2: 4, 3: 2}
    #     table[i] = val

    # sorted_table = sorted(table.items(), key=lambda x: x[1])
    # # [(1, 1), (3, 2), (0, 3), (2, 4)]

    # for i in sorted_table:
    #     for j in range(len(i)):
    #         print(i[j])
    stack, third = [], float('-inf')
    
    for num in reversed(nums):
        if num < third: # third = 2
            return True
        while stack and stack[-1] < num: 
            third = stack.pop() # 10
        stack.append(num) # 4 в стак - 3 в стак # 1
        print(num)
    return False
        
nums = [1,10,3,4]
print(find132pattern(nums))