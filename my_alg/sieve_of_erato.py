# Текстовое решение:
# 1. Создаём список чисел + отмечаем числа 0 и 1 - False
# 2. В диапозоне от 2 до n, при наличии числа, выполняем условие:
# начиная со степени числа, до n + 1, с шагом в простое число - False
# 3. Возвращаем наш список чисел

def erato(n):
    numbers = list(range(n+1))
    numbers[0] = numbers [1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers
