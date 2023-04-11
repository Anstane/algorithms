# Номер посылки - 85479282

from typing import List


class StackIsEmptyError(Exception):
    """Ошибка возникает, если стек был пуст."""
    pass


class Stack:
    def __init__(self):
        self.__array = []

    def push(self, obj):
        self.__array.append(obj)

    def pop(self):
        if len(self.__array) == 0:
            raise StackIsEmptyError('error')
        return self.__array.pop()


def calculation(array: List[str]) -> str:
    calculator = Stack()
    operations = {
        '+': lambda x, y: y + x,
        '-': lambda x, y: y - x,
        '*': lambda x, y: y * x,
        '/': lambda x, y: y // x
    }
    for value in array:
        if value not in operations:
            if value.isdigit():
                calculator.push(value)
            else:
                raise ValueError('Ошибка передаваемых данных')
        else:
            x = int(calculator.pop())
            y = int(calculator.pop())
            calculator.push(str(operations[value](x, y)))
    return calculator.pop()


if __name__ == '__main__':
    calculator_input = input().split()
    print(calculation(calculator_input))
