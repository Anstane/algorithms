import re


def decodeAtIndex(s: str, k: int) -> str:
    length = 0 # Переменная длины
    i = 0 # Счётчик

    while length < k: # До тех пор, пока строка короче k
        if s[i].isdigit():
            length *= int(s[i]) # Если число - умножаем на него
        else:
            length += 1 # Если бука - +1
        i += 1 # Каждый шаг +1
    
    for j in range(i-1, -1, -1): # В обратном порядке идём по строке
        char = s[j] # Берём из строки знак
        if char.isdigit(): # Если это число
            length //= int(char) # Делим длину общую на число
            k %= length # k делим на длину остаточную
        else: # Если это не число
            if k == 0 or k == length: # Если k = 0 или k = длине
                return char # Возвращаем символ
            length -= 1 # Или просто 1 забираем из длины

    # res = re.sub(r'[^a-zA-Z]', '', s)
    # rei = re.sub(r'[^0-9]', '', s)

    # if len(res) <= 2 and k <= 1:
    #     return res[k - 1]

    # new_string = ''
    
    # for char in s:
    #     if char.isdigit():
    #         new_string += char * int(char)
    #     else:
    #         new_string += char

    # return new_string[k - 1]


if __name__ == '__main__':
    s = "leet2code3"
    k = 10
    print(decodeAtIndex(s, k))
