from typing import List

"""Проверка на 3 числа в ряд"""
def check_parity(numbers: List[int]) -> bool:
	odd = []
	even = []

	for i in numbers:
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)

	if len(odd) == 3 or len(even) == 3:
		return 'WIN'
	else:
		return 'FAIL'

numbers = map(int, input().strip().split())
print(check_parity(numbers))
