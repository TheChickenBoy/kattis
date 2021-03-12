l = 0
h = 1001
while True:
    g = (l+h)//2
    print(g)
    s = input()
    if s == 'lower':
        h = g
    elif s == 'higher':
        l = g
    else:
        exit()