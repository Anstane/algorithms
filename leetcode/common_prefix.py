from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    min_word = len(min(strs, key=len))
    preffix = ''

    for i in range(min_word):

        pivot = strs[0][i] 
        window = [word[i] for word in strs]
        
        if all([char == pivot for char in window]):
            preffix += pivot
        else:
            break
    
    return preffix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
