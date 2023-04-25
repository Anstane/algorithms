arr_one = input()
arr_two = input()

a = 0
for val in arr_two:
    if a == len(arr_one):
        break
    if val == arr_one[a]:
        a += 1

print(a == len(arr_one))
