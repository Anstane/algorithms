# def findTheDifference(s: str, t: str) -> str:
#     list_s = list(s)
#     list_t = list(t)
#     list_s.sort()
#     list_t.sort()
#     for i in range(len(list_s)):
#         if list_t[0] == list_s[i]:
#             list_t.pop(0)
#     return list_t[0]


def findTheDifference(s: str, t: str) -> str:
    result = 0
    for char in s + t:
        result ^= ord(char)
    return chr(result)

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))