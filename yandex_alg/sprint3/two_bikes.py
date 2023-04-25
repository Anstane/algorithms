def binary_rec(array, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if x == array[mid]:
        return mid
    elif x < array[mid]:
        return binary_rec(array, x, left, mid)
    else:
        return binary_rec(array, x, mid + 1, right)

array = [i for i in range(10)]
x = 4

print(binary_rec(array, x, left=0, right=len(array)))

m = int(input())
array = [int(i) for i in input().split()]
x = int(input())

def two_bikes(array, x, left, right):
    mid = (left + right) // 2
    if x < array[mid]:
        return two_bikes(array, x, left, mid)
    else:
        if x > array[right]:
            return -1
        elif x == array[mid]:
            if array[mid] == array[mid - 1]:
                return mid
            else:
                return mid + 1
        else:
            return right + 1

print(two_bikes(array, x, left=0, right=len(array)-1), end=' ')
print(two_bikes(array, x*2, left=0, right=len(array)-1), end=' ')

def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)

days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())

print(binarySearch(money, price, left = 0, right = len(money)), end=' ')
print(binarySearch(money, price * 2, left = 0, right = len(money)), end=' ')


m = int(input())
array = [int(i) for i in input().split()]
price = int(input())

def two_bikes(array, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if array[mid] >= price and (array[mid - 1] < price or mid == 0):
        return mid + 1
    elif price <= array[mid]:
        return two_bikes(array, price, left, mid)
    else:
        return two_bikes(array, price, mid + 1, right)

index_one = two_bikes(array, price, left=0, right=len(array))
index_two = two_bikes(array, price*2, left=0, right=len(array))
print(f"{index_one} {index_two}")
