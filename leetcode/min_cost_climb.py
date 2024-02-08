from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    array = [0] * n
    array[0] = cost[0]
    array[1] = cost[1]
    for i in range(2, n): 
        array[i] = cost[i] + min(array[i - 1], array[i - 2])
    return min(array[n - 1], array[n - 2])


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
