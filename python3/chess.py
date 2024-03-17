from sys import stdin

board = {'A': 1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
for _ in range(int(stdin.readline())):
    sc,sn,ec,en = stdin.readline().strip().split()
    sc = board[sc]
    ec = board[ec]
    sn = int(sn)
    en = int(en)

    if(sc+sn+ec+en) % 2 != 0:
        print("impossible")
        continue

    move = [(sc,sn)]
    while move:
        cur = move.pop(0)
        x = cur[0]
        y = cur[1]

        if x == ec and y == en:
            break
        for i in range(1,9):
            