def tower_of_champain(poured, query_row, query_glass):
    tower = [[0] * (i + 1) for i in range(query_row + 1)] # Строим башню полную нулей
    tower[0][0] = poured # Заполняем первый массив матрицы
    
    for row in range(query_row): # Перебираем ряды
        for glass in range(len(tower[row])): # Перебираем стаканы из каждого ряда
            excess = (tower[row][glass] - 1) / 2.0 # Исходное наполнение мы разделяем между стаканами
            if excess > 0:
                tower[row + 1][glass] += excess # Левый стакан заполняем 
                tower[row + 1][glass + 1] += excess # Правый стакан
    return min(1.0, tower[query_row][query_glass]) # Если в стакане больше 1.0 - вернём 1.0

    # Initialize the tower with all glasses having 0 poured champagne
    # tower = [[0.0] * k for k in range(1, 102)]
    # tower[0][0] = poured  # Pour the initial amount of champagne
    # print(tower)
    
    # # Traverse each row and update the champagne in each glass
    # for i in range(query_row + 1):
    #     for j in range(i + 1):
    #         overflow = (tower[i][j] - 1.0) / 2.0  # Calculate overflow
    #         if overflow > 0:
    #             tower[i + 1][j] += overflow
    #             tower[i + 1][j + 1] += overflow
    
    # # Return the amount of champagne in the specified glass
    # return min(1.0, tower[query_row][query_glass])  


# poured = 100000009
# query_row = 33
# query_glass = 17
poured = 2
query_row = 1
query_glass = 1

print(tower_of_champain(poured, query_row, query_glass))
