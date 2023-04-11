import re

def is_palindrome(line: str) -> bool:

    new_line = re.sub(r'[^\w]','', line.lower())

    return new_line == new_line[::-1]

print(is_palindrome(input()))
