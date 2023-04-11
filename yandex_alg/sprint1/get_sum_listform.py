from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
	result = number_list + k
	result = ' '.join(str(result))
	return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = int(''.join(input().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(get_sum(number_list, k))