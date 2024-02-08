from typing import List
from collections import deque


tokens = ["2","1","+","3","*"]


def evalRPN(tokens: List[str]) -> int:
    stack = deque()
    operand = ["+", "-", "*", "/"]
    for i in tokens:
        if i not in operand:
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == "+":
                stack.append(num1 + num2)
            elif i == "-":
                stack.append(num1 - num2)
            elif i == "*":
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))
    
    return stack

print(*evalRPN(tokens))
