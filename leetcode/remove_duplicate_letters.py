def removeDuplicateLetters(s: str) -> str:
    table = {}
    stack = []
    visited = set()

    for i in range(len(s)): # {'c': 7, 'b': 6, 'a': 2, 'd': 4}
        table[s[i]] = i

    for i in range(len(s)): # Перебираем буквы

        if s[i] not in visited: # Если эту букву ещё не трогали
            while (stack and stack[-1] > s[i] and table[stack[-1]] > i): # b > a and 6 > 3
                visited.remove(stack.pop()) # Сносим все буквы до a и делаем её началом

            stack.append(s[i]) # Добавляем буквы в стек
            visited.add(s[i]) # Добавляем буквы в множество

    return ''.join(stack)

# string = "".join(sorted(i for i in table.keys()))
# string_list = [i for i in table.keys()]
# return sorted(string_list, key=str.upper)

s = "cbacdcbc" # "acdb"
print(removeDuplicateLetters(s))