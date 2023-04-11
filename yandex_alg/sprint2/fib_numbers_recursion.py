n = int(input())

def recursion(n):
    if n in (0, 1):
        return 1
    else: 
        # Сначала мы доходим до минимальных чисел (0 и 1) и 
        # потом производим операции в обратном порядке.
        return recursion(n - 1) + recursion(n - 2)

print(recursion(n))
