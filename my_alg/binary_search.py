from random import randint


"""
Создаём список случайных числен в диапозоне 10
и сортируем его.
"""
list = []
for i in range(10):
    list.append(randint(1, 100))
list.sort()

print(list)

value = int(input()) # Печатаем с клавиатуры нужное число

# Получаем индексы минимального, максимального и среднего
min = 0
max = len(list) - 1
mid = len(list) // 2

"""
1. Если число с клавиатуры больше или меньше центрального:
- Больше: Минимальное = Центральное + 1
- Меньше: Максимальное = Центральное - 1
2. Обновлем центральное число на каждом цикле
3. Возвращаем центральное число.
"""
while list[mid] != value and min <= max:
    if value > list[mid]:
        min = mid + 1
    else:
        max = mid - 1
    mid = (min + max) // 2
            
if min > max:
    print('No value')
else:
    print('ID=', mid)
