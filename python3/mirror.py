for q in range(int(input())):
    r,c = map(int,input().split())
    d = []
    s=""
    for w in range(r):
        l = input()
        d.append(l)

    for i in range(r):
        for j in range(c):
            s += d[r-1-i][c-1-j]
        s+='\n'
    print("Test " + str(q+1))
    print(s)


"""
 l[0][0] = L[i][j]
 l[0][1] = L[i][j-1]

 l[1][0] = L[i-1][j]
 l[1][1] = L[i-1][j-1]

 .*    . .
 ..    * .
"""
