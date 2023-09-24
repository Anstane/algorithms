from typing import List


def longestStrChain(words: List[str]) -> int:
    words.sort(key=len) # Сортируем по длине
    table = {}
    maximum = 0
    for word in words: # Перебираем слова в массиве
        table[word] = 1 # Берём слово и присваеваем значение 1
        for i in range(len(word)):
            prev_word = word[:i] + word[i + 1:] # Перебираем все возможности предыдущего слова
            if prev_word in table: # Если это слово есть в словаре
                table[word] = max(table[word], table[prev_word] + 1) # Записываем вес этого слова
        maximum = max(maximum, table[word]) # Если это слово больше текущего в переменной - перезаписываем
    return maximum


words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(longestStrChain(words))
