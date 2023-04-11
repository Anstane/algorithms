"""Вычисляем длину с помощью функции max и key=len"""
def get_longest_word(sentence: str) -> str:
    result = max(sentence, key=len)
    return result

def read_input() -> str:
    n = input()
    sentence = list(input().strip().split())
    return sentence

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))