for q in range(int(input())):
    r,c = map(int,input().split())
    d = []
    t = []
    for w in range(r):
        l = input()
        d.append(l)
        t.append(l)

    for i in range(r):
        for j in range(c):
            t[i][j] = d[r-1-i][c-1-j]
    print(t)


"""
 l[0][0] = L[i][j]
 l[0][1] = L[i][j-1]

 l[1][0] = L[i-1][j]
 l[1][1] = L[i-1][j-1]

 .*    . .
 ..    * .
"""
