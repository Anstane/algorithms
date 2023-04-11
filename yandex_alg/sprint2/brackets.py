# {[()]}
# ({]})

def is_correct_bracket_seq(brackets):
    stack = [] # Создаём пустой стэк
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    if not brackets: # Проверка на пустоту
        return True
    elif brackets[0] in close_brackets: # Если начинается с закрывающих - сразу False
        return False
    for character in brackets:
        if character in open_brackets:
            stack.append(open_brackets.index(character)) # Если открывающая ковычка - добавляем в стэк c индексом от массива выше
        elif character in close_brackets:
            if len(stack) != 0 and stack[-1] == close_brackets.index(character): # Если массив не пустой и [-1] совпадает с индексом - удаляем
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(is_correct_bracket_seq(list(input())))


def is_correct_bracket_seq(brackets):
    counter = 0
    open = ['(', '{', '[']
    close = [')', '}', ']']
    for i in brackets:
        if i in open:
            counter += 1
        if i in close:
            counter -= 1
    return counter == 0

print(is_correct_bracket_seq(list(input())))