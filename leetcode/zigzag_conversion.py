def convert(s: str, numRows: int) -> str:
    if numRows == 1 or len(s) <= numRows:
        return s

    zigzag_matrix = ['' for _ in range(numRows)]
    print(zigzag_matrix)
    direction = 1
    row = 0

    for char in s:
        zigzag_matrix[row] += char
        print(zigzag_matrix)
        if row == 0:
            direction = 1
        elif row == numRows - 1:
            direction = -1
        row += direction
    
    result = ''.join(zigzag_matrix)
    return result


s = "PAYPALISHIRING" # Output: PINALSIGYAHRPI
numRows = 4
print(convert(s, numRows))
