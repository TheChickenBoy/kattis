from sys import stdin
king   = 100
queen  = 90 
rook   = 80
bishop = 70 
knight = 60
pawn   = 0

alph = {
    30:'h',
    26:'g',
    22:'f',
    18:'e',
    14:'d',
    10:'c',
    6:'b',
    2:'a'
}


white = {}
black = {}

def check(c):
    if c == 'k':
        return king, 'K'
    elif c == 'q':
        return queen, 'Q'
    elif c == 'r':
        return rook, 'R'
    elif c == 'b':
        return bishop, 'B'
    elif c == 'n':
        return knight, 'N'
    else:
        return pawn, ''

board = []
for l in stdin:
    board.append(l)

row = 1
for i in range(8,0,-1):
    r = board[row]
    for j in range(2, 31, 4):
        if r[j] == '.' or r[j] == ':':
            continue
        
        elif r[j].isupper():
            val, c = check(r[j].lower())
            white[c+alph[j]+str(i)] = val-i
        else:
            val, c = check(r[j])
            black[c+alph[j]+str(i)] = val+i
    row +=2

white = {k: v for k, v in sorted(white.items(), key=lambda item: item[1], reverse=True)}
black = {k: v for k, v in sorted(black.items(), key=lambda item: item[1], reverse=True)}
print("White:", ','.join(map(str,list(white.keys()))))
print("Black:",','.join(map(str,list(black.keys()))))
