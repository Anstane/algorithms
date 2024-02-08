params = input().split()
n, t, s = map(int, params)

speeds = input().split()
v = list(map(int, speeds))


def count_overtakes(n, t, s, v):
    overtakes = 0

    for i in range(1, n):
        if v[0] > v[i]:
            relative_position = ((v[0] / s) - (v[i] / s)) * t
            overtakes += relative_position

    if overtakes != 0:
        overtakes -= len(v) - 1

    return overtakes
    
result = count_overtakes(n, t, s, v)
print(int(result))
