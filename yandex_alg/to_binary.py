def to_binary(number: int) -> str:
    binary = []

    if number == 0:
        print(0)
    else:
        while number != 0:
            x = number % 2
            number = number // 2
            binary.append(x)
        else:
            print(''.join(map(str, (binary[::-1]))))

def read_input() -> int:

    return int(input().strip())

to_binary(read_input())
