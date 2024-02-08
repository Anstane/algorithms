from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
        strength = [(sum(soldiers), row) for row, soldiers in enumerate(mat)] # Составляем массив значений и индексов
        strength.sort(key=lambda x: (x[0], x[1])) # Сортируем индекс и значеине
        return [val[1] for val in strength[:k]] # Возвращаем массив значений - обрезанный по k


mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]

k = 3

print(kWeakestRows(mat, k))
