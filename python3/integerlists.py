for i in range(0,int(input())):
    rev = False
    bapc = input()
    n = int(input())
    l = input()[1:-1].split(',')
    df = db = 0
    for c in bapc:
        if c == 'R':
            rev = not rev
            t = df
            df = db
            db = t
        else:
            df+=1

    if df+db>n or ('D' in bapc and n==0):
        print("error")
    else:
        if rev:
            l.reverse()
        print('['+(','.join(l[df:len(l)-db]))+']')
