"""Передаём условие функции и подставляем значения"""
def evaluate_function(a: int, b: int, c: int, x: int) -> int:
	result = a * (x ** 2) + b * x + c
	return result

a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
