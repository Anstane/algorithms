n, k = (int(i) for i in input().split())

def fib(n, k):
    array = [1, 1]
    if n < 2:
        fib = 1
    else:
        for i in range(n - 1):
            number = array[0] + array[1]
            array[0] = array[1]
            array[1] = number
            fib = array[1]
    return fib

print(fib(n, k) % 10 ** k)