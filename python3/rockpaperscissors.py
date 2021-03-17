def win(m1,m2):
    if m1 == m2:
        return 0
    elif m1 == "rock" and m2 == "scissors" or m1 == "paper" and m2 == "rock" or m1 == "scissors" and m2 == "paper":
        return 1
    else:
        return 2

while True:
    inp = list(map(int,input().split()))
    if len(inp) == 1:
        exit()

    wins = {str(k+1):0 for k in range(inp[0])}
    loss = {str(k+1):0 for k in range(inp[0])}
    for _ in range(int((inp[1]*inp[0]*(inp[0]-1))/2)):
        s = input().split()
        res = win(s[1],s[3])
        if res == 1:
            wins[s[0]] += 1
            loss[s[2]] += 1
        elif res == 2:
            wins[s[2]] += 1
            loss[s[0]] += 1
    
    for k in wins.keys():
        if wins[k] + loss[k] == 0:
            print('-')
        else:
            print("{:.3f}".format((wins[k])/(wins[k] + loss[k])))