def longestPalindrome(s: str) -> str:
    left = 0
    max_length = 0
    hash_map = {}
    n = len(s)

    for right in range(n):
        if s[right] not in hash_map or hash_map[s[right]] < left:
            hash_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        else:
            left = hash_map[s[right]] + 1
            hash_map[s[right]] = right

    return max_length

s = "babad"
print(longestPalindrome(s))
