def isSubsequence(s: str, t: str) -> bool:
    counter = 0

    for value in t: # Итерируемся по длинной строчке
        if counter == len(s): # Если счётчик == длине короткой строчки
            break
        if value == s[counter]: # Если буква есть в короткой строчке
            counter += 1

    return counter == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
