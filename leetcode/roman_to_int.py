def romanToInt(s: str) -> int:
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    counter = 0

    for i in range(len(s)):
        if roman_int[s[i]] > roman_int[s[i - 1]] and i != 0:
            counter += roman_int[s[i]] - roman_int[s[i - 1]] * 2
        else:
            counter += roman_int[s[i]]

    return counter

s = "MCMXCIV"
print(romanToInt(s))