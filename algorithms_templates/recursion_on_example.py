num = int(input())

def brackets(num, brack, left, right):
    """Реализация рекурсии на примере задачи.
    
    Создаём две переменных ->
    заполняем сначала первую переменную ->
    затем вторую ->
    возвращаем склеянный результат.
    """
    if left == num and right == num:
        print(brack)
    else:
        if right < num:
            brackets(num, brack + '(', left, right + 1)
        if left < right:
            brackets(num, brack + ')', left + 1, right)


brackets(num, brack='', left=0, right=0)
