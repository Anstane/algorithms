from typing import List

def factorize(x: int) -> List[int]:
	final_num = []
	y = 2
	while y * y <= x: # 4 / 9 / 16 - Если число делится на степень простого - тогда оно делится и на само число
		if x % y == 0: # Делится на 2 .. .без остатка - отрабатывает if
			x = x / y # Число делится на y и заменяет текущее
			final_num.append(y) # Записывается первое число разделённое на составное
		else:
			y += 1
	if x > 1: # Число делится на самого себя - добавляем его сразу в список
		final_num.append(int(x))
	return final_num

result = factorize(int(input()))
print(" ".join(map(str, result)))
