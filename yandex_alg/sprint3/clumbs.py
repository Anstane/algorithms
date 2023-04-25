n = int(input())

clumbs = []

for _ in range(n):
    clumbs.append(list(map(int, input().split())))

def clumbs_merge(clumbs):
    clumbs.sort() # Сортируем массив
    new_clumbs = [] # Создаём новый массив, в который будем записывать значения
    left = clumbs[0][0]
    right = clumbs[0][1] # Создаём левую и правую сторону, на которые будем ориентироваться в цикле
    for i in range(n - 1):
        if right < clumbs[i + 1][0]: # Если левое значение i + 1 < правого i
            new_clumbs.append("{} {}".format(left, right)) # Добавляем в массив изначальное значение
            left = clumbs[i + 1][0] # Переписываем, что лево = i + 1[0]
            right = clumbs[i + 1][1] # Право = i + 1[1]
        if right < clumbs[i + 1][1]: # Если новое право < i + 1[1]
            right = clumbs[i + 1][1] # Перезаписываем его
    new_clumbs.append("{} {}".format(left, right)) # Выходя из массива записываем последнее значение
    
    return new_clumbs

new_clumbs = clumbs_merge(clumbs)

for i in range(len(new_clumbs)):
    print(new_clumbs[i])
