import sys

k = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def counting_sort(array):
    counting_values = [0] * 3

    for value in array:
        counting_values[value] += 1

    result = [num for num, count in enumerate(counting_values) for i in range(count)]

    return result

print(*counting_sort(nums))