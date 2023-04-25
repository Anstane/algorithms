def erato(n):
    """Реализация алгоритма решета Эратосфена.
    
    Логика работы:
    1) Создаём массив значений в заданном диапазоне;
    2) Ставим для значение 0 и 1 изначально False;
    3) Начиная со второго числа выполняем заданное условие ->
    если значение не False ->
    все числа кратные num = False.
    """
    numbers = list(range(n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers
