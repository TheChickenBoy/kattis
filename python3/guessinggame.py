while True:
    high = 11
    low = 0
    while True:
        guess = int(input())
        if guess == 0:
            exit()
        
        ans = input().split()[1]
        if ans == 'high':
            high = min(high,guess)
        elif ans == 'low':
            low = max(low,guess)
        else:
            print("Stan may be honest") if guess>low and guess<high else print("Stan is dishonest")
            break