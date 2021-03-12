N = 8

# helper matrices 
slashCode = [[0 for i in range(N)] 
                for j in range(N)]
backslashCode = [[0 for i in range(N)] 
                    for j in range(N)]

# arrays to tell us which rows are occupied 
rowLookup = [False] * N
colLookup = [False] * N

# keep two arrays to tell us 
# which diagonals are occupied 
x = 2 * N - 1
slashCodeLookup = [False] * x
backslashCodeLookup = [False] * x

# initialize helper matrices 
for rr in range(N):
    for cc in range(N):
        slashCode[rr][cc] = rr + cc
        backslashCode[rr][cc] = rr - cc + 7

for i in range(N):
    l = input()
    try:
        x = l.index('*')
    except ValueError:
        print("invalid")
        exit()
    

    if(rowLookup[i] or colLookup[x] or slashCodeLookup[slashCode[i][x]] or backslashCodeLookup[backslashCode[i][x]]):
        print("invalid")
        exit()
    rowLookup[i] = True
    colLookup[x] = True
    slashCodeLookup[slashCode[i][x]] = True
    backslashCodeLookup[backslashCode[i][x]] = True
    #print(x)
print("valid")
exit()