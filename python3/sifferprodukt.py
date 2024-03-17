s = input()
r = 1

while True:
    for c in s:
        if c == '0':
            r*=1
        else:
            r*=int(c)
    if r%10 == 0 and r < 10:
        print(r%10)
        exit()
    if r < 10:
        print(r)
        exit()
    s = str(r)
    r = 1