n = int(input()) # Строки
m = int(input()) # Столбцы 

# Создаём списки в количестве строк
matrix = []
for i in range(n):
	matrix.append(list(map(int, input().strip().split())))

row = int(input()) # Индекс строки
col = int(input()) # Индекс столбца

def find_neighborhood(n, m, row, col):
	neighborhood = [] # Создаём список для будущих координат

	# Проверяем существует ли соседнее число
	if row + 1 < n:
		neighborhood.append(matrix[row+1][col])
	if col + 1 < m:
		neighborhood.append(matrix[row][col+1])
	if row - 1 >= 0:
		neighborhood.append(matrix[row-1][col])
	if col - 1 >= 0:
		neighborhood.append(matrix[row][col-1])

	neighborhood.sort() # Сортируем полученные числа по возрастанию

	return (' '.join(map(str, (neighborhood))))

print(find_neighborhood(n, m, row, col))
	