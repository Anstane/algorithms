def gen_binary(n, brackets, left, right):
    if left == n and right == n:
        print(brackets)
    else:
        if left < n:
            gen_binary(n, brackets + '(', left + 1, right)
        if right < left:
            gen_binary(n, brackets + ')', left, right + 1)

n = int(input())

gen_binary(n, brackets='', left=0, right=0)
