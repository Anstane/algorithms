def reverseWords(s: str) -> str:
    # new_list = s.split(' ')
    # result = ' '.join([''.join(i[::-1]) for i in new_list])
    # return result

    return ' '.join(map(lambda x: x[::-1], s.split()))


# "s'teL ekat edoCteeL tsetnoc"
s = "Let's take LeetCode contest"
print(reverseWords(s))
