def intToRoman(num: int) -> str:
    roman_int = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''

    for val in roman_int.keys():
        while num >= val:
            result += roman_int[val]
            num -= val

    return result

num = 1994
print(intToRoman(num))
