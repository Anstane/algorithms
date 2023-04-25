n = int(input())
array = [list(map(int, i)) for i in input().split()]

"""Тут мы сравниваем только первое число и большое - становится вперёд."""
def bubble_sort(n, array):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j][0] < array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    another_array = []

    for i in range(n):
        another_array.extend(array[i])
    
    print(*(another_array), sep='')

bubble_sort(n, array)

n = int(input())
array = input().split()

"""Просто сумируем строки - большое значение меняется местами."""
def biggest_number(n, array):
    for i in range(n - 1):
        for j in range(n - i - 1):
            first_var = array[j] + array[j + 1]
            second_var = array[j + 1] + array[j]
            if first_var < second_var:
                array[j], array[j + 1] = array[j + 1], array[j]
    return ''.join(array)

print(biggest_number(n, array))