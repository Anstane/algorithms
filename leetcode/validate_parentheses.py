from collections import deque


def isValid(s: str) -> bool:
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']

    if s is None:
        return False
    
    if s[0] in close_bracket:
        return False

    stack = []

    for i in s:
        if i in open_bracket:
            stack.append(open_bracket.index(i))
        elif i in close_bracket:
            if len(stack) != 0 and stack[-1] == close_bracket.index(i):
                stack.pop()
            else:
                return False

    return len(stack) == 0

s = "()"
print(isValid(s))
