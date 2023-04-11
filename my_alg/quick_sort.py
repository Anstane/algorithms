from random import randint

array = []
for i in range(10):
    array.append(randint(1, 100))

print(array)

"""
Алгоритм быстрой сортировки через рекурсию.
Логика работы:
1) Ищем базовый случай для выхода из рекурсии
2) Ищем опорный элемент
3) Создаём два массива меньше и больше опорного элемента
4) Повторить, пока не дойдём до базового случая
"""
def quick_sort(array):
    if len(array) < 2: # Базовый случай
        return array
    else:
        pivot = array[0] # Опорный элемент
        low = [i for i in array[1:] if i <= pivot] # Меньше опорного элемента
        high = [i for i in array[1:] if i > pivot] # Больше опорного элемента
        return quick_sort(low) + [pivot] + quick_sort(high)

print(quick_sort(array))
