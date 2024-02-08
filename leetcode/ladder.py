from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    array = [0] * n

    array[0] = cost[0]
    array[1] = cost[1]

    for num in range(2, n):
        array[num] = cost[num] + min(array[num - 1], array[num - 2])

    return min(array[n - 1], array[n - 2])


cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))