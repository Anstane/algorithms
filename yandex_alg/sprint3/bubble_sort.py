n = int(input())
array = [int(i) for i in input().split()]

def minimum_sort(n, array): # Фактически - choosing sort с формальным сохранением устойчивости
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
        print(*array)

# minimum_sort(n, array)

def bubble_sort(n, array):
    flag = 1
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = 1

        if flag == 1:
            print(*array)
            flag = 0

bubble_sort(n, array)