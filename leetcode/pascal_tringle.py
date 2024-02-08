from typing import List


def getRow(rowIndex: int) -> List[int]:
    triangle = [[0] * (i + 1) for i in range(rowIndex + 1)]

    for row in range(rowIndex + 1):
        for num in range(len(triangle[row])):
            triangle[row][0] = triangle[row][-1] = 1
            if triangle[row][num] == 0:
                triangle[row][num] = (
                    triangle[row - 1][num - 1] + triangle[row - 1][num]
                )

    return triangle[rowIndex]


rowIndex = 4
print(getRow(rowIndex))
