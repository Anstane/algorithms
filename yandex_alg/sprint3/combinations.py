n = [int(i) for i in ''.join(input().split())]

operations = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

result = []

def combinations(n, result, comb=''):
    if n == []:
        result.append(comb)
        return
    else:
        for i in operations[n[0]]:
            combinations(n[1:], result, comb + i)

combinations(n, result)

new_array = []

for i in result:
    new_array.append(i)

print(*(new_array))