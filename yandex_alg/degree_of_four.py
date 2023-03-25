import math

def is_power_of_four(number: int) -> bool:

    x = math.log(number, 4)

    return int(x) == float(x)

print(is_power_of_four(int(input())))
