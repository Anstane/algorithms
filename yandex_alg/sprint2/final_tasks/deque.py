# Номер посылки - 85479153

from typing import List


class DequeIsEmptyError(Exception):
    """Возникает когда дек пустой."""
    pass


class DequeIsFullError(Exception):
    """Возникает когда дек полный."""
    pass


class Deque:
    def __init__(self, m):
        self.__deque = [None] * m
        self.__max_elements = m
        self.__head = 0
        self.__tail = 0
        self.__size_of_deque = 0

    def is_empty(self):
        return self.__size_of_deque == 0

    def push_front(self, value):
        if self.__size_of_deque == self.__max_elements:
            raise DequeIsFullError
        if self.__deque[self.__head] is None:
            self.__deque[self.__head] = value
            self.__size_of_deque += 1
        else:
            self.__head = (self.__head - 1) % self.__max_elements
            self.__deque[self.__head] = value
            self.__size_of_deque += 1

    def push_back(self, value):
        if self.__size_of_deque == self.__max_elements:
            raise DequeIsFullError
        if self.__deque[self.__tail] is None:
            self.__deque[self.__tail] = value
            self.__size_of_deque += 1
        else:
            self.__tail = (self.__tail + 1) % self.__max_elements
            self.__deque[self.__tail] = value
            self.__size_of_deque += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeIsEmptyError
        value = self.__deque[self.__head]
        self.__deque[self.__head] = None
        if self.__deque[(self.__head + 1) % self.__max_elements] is not None:
            self.__head = (self.__head + 1) % self.__max_elements
        self.__size_of_deque -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise DequeIsEmptyError
        value = self.__deque[self.__tail]
        self.__deque[self.__tail] = None
        if self.__deque[(self.__tail - 1) % self.__max_elements] is not None:
            self.__tail = (self.__tail - 1) % self.__max_elements
        self.__size_of_deque -= 1
        return value


def deque_procedures(max_len: int, array: List[str]):
    deque = Deque(max_len)

    for command in array:
        try:
            if len(command) == 1:
                print(getattr(deque, command[0])())
            else:
                getattr(deque, command[0])(int(command[1]))
        except DequeIsFullError:
            print('error')
        except DequeIsEmptyError:
            print('error')


if __name__ == '__main__':
    length_array = int(input())
    max_length_of_deque = int(input())
    array = [input().split() for _ in range(length_array)]
    deque_procedures(max_length_of_deque, array)
