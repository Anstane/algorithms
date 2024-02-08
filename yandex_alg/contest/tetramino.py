def read_input_matrix_update():
    matrix_input = [input() for _ in range(8)]
    matrix = [list(row + '*') for row in matrix_input]
    matrix.append(['*'] * 9)

    return matrix


def count_tetramino():
    counter = 0
    matrix = read_input_matrix_update()

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == '.':
                if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i][j - 1] == '.':
                    counter += 1
                if matrix[i][j] == matrix[i][j + 1] == matrix[i - 1][j] == matrix[i][j - 1] == '.':
                    counter += 1
                if matrix[i][j] == matrix[i - 1][j] == matrix[i + 1][j] == matrix[i][j + 1] == '.':
                    counter += 1
                if matrix[i][j] == matrix[i - 1][j] == matrix[i + 1][j] == matrix[i][j - 1] == '.':
                    counter += 1

    return counter


if __name__ == '__main__':
    result = count_tetramino()
    print(result)
