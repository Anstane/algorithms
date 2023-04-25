import array

"""
Принимиет два отсортированных массива и сливает в один, и возвращает его.
Первый массив - [left, mid)
Второй массив - [mid, right)
"""
def merge(arr: list, left: int, mid: int, right: int) -> array:

    left_arr = arr[left:mid] # Создаём лево
    right_arr = arr[mid:right] # Создаём право

    i, j = 0, 0 # Грубо говоря 2 счётчика
    result = []

    while i < len(left_arr) and j < len(right_arr): # Тут прибавляем число из левого массива и правого
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    
    result += left_arr[i:] # Прибавляем остаток
    result += right_arr[j:]

    arr[left:right] = result # Переписываем массив

    return arr

"""
Принимает подмассив, который нужно отсортировать.
Ничего не возвращает. Разбивает на две половинки, а затем рекурсивно возвращает.
"""
def merge_sort(arr: list, left: int, right: int) -> None:
    if left < right - 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid) # Это штука просто делит входящий массиво на левое и правое
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right) # А тут они уже наоборот склеиваются
        return arr

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
