def backtrack(r):
    if r==n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag or board[r][c] == '-':
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = 'Q'

        backtrack(r+1)
        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '.'

while True:
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board=[]
    holes = {}
    n,m = map(int,input().split())
    if n == m == 0:
        exit()
    for i in range(m):
        t1,t2 = map(int,input().split())
        if t1 in holes:
            holes[t1].append(t2)
        else:
            holes[t1] = [t2]
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append('.')
            if len(holes) == 0:
                continue
            if i in holes:
                if j in holes[i]:
                    row[j] = "-"

        board.append(row)
    backtrack(0)
    print(len(res))