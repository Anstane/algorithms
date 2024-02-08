def winnerOfGame(colors: str) -> bool:
    alice, bob = 0, 0
    count = 1
    
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]: # AAA
            count += 1 # 3
        else:
            if colors[i - 1] == 'A':
                alice += max(0, count - 2)
            else:
                bob += max(0, count - 2)
            count = 1

    if colors[-1] == 'A':
        alice += max(0, count - 2)
    else:
        bob += max(0, count - 2)
    
    return alice > bob

colors = "AAABABB"
print(winnerOfGame(colors))
