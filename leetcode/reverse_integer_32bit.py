import math


def reverse(x: int) -> int:
    max_int = 2 ** 31 - 1
    min_int = -2 ** 31
    rev_num = 0

    while x != 0:
        if rev_num > max_int / 10 or rev_num < min_int / 10:
            return 0
        digit = x % 10 if x > 0 else x % - 10
        rev_num = rev_num * 10 + digit
        x = math.trunc(x / 10)

    return rev_num

x = -123
print(reverse(x))
