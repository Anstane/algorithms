n = int(input())
temperature = input().split()


def chaos_of_weather(temperature):
	days = list(map(int, temperature)) # Преобразуем данные в список int`ов
	counter = 0

	# Начиная со второго элемента и без последнего проверяем заданное условие
	for i in range(1, len(temperature) - 1):
		if days[i-1] < days[i] > days[i+1]:
			counter += 1

	# Проверяем, что элеметов больше чем один, делая запрос ко второму элементу
	try:
		if days[1]:

			# Проверяем оставшиеся индексы [0] и [-1]
			if days[0] > days[1]:
				counter += 1

			if days[-1] > days[-2]:
				counter += 1

	# Если элемент только один - добавляем 1 к счётчику и возвращаем его
	except Exception:
		counter += 1

	return counter

print(chaos_of_weather(temperature))
