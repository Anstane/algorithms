from typing import List
import bisect


def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
    # rev_sorted_flowers = sorted(flowers, key=lambda x: x[1], reverse=True)
    # array_of_zeros = [0 for i in range(rev_sorted_flowers[0][1])]
    
    # for i in flowers:
    #     for j in range(i[0] - 1, i[1]):
    #         array_of_zeros[j] += 1
    
    # for i in range(len(people)):
    #     if people[i] - 1 < len(array_of_zeros):
    #         people[i] = array_of_zeros[people[i] - 1]
    #     else:
    #         people[i] = 0
    
    # return people

    start = sorted([s for s, e in flowers]) # Левые числа
    end = sorted([e for s, e in flowers]) # Правые числа
    print([bisect.bisect_right(start, t) - bisect.bisect_left(end, t) for t in people]) 

    # Самое правое - насколько можно переместиться
    # Минус самое левое насколько можно переместиться


flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]

print(fullBloomFlowers(flowers, people))