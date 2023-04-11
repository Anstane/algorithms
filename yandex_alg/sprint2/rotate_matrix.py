row = int(input())
col = int(input())
matrix = []
for i in range(row):
    matrix.append(input().strip().split())

def new_matrix(matrix):
    new_matrix = [[0]*row for i in range(col)] # Забиваем матрицу нужных размеров 0
    for i in range(row):
        for j in range(col):
            new_matrix[j][i] = matrix[i][j] # Заменяем местами индексы строк и столбцов
    return new_matrix

for i in new_matrix(matrix):
    print(' '.join(i))

# https://www.cyberforum.ru/python-beginners/thread2436330.html