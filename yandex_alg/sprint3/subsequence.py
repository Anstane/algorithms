arr_one = input()
arr_two = input()

a = 0
for val in arr_two: # Идём по длинному массиву
    if a == len(arr_one): # Выход из цикла заранее, если длина сошлась
        break
    if val == arr_one[a]: # Если буква из второго массива == букве из первого
        a += 1

print(a == len(arr_one))
