norm_r = "+---+---+---+---+---+---+---+---+"
row1 = ['|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|']
row2 = ['|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|']
row3 = ['|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|']
row4 = ['|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|']
row5 = ['|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|']
row6 = ['|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|']
row7 = ['|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|']
row8 = ['|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|','.','.','.','|',':',':',':','|']

alph = {
    'h':30,
    'g':26,
    'f':22,
    'e':18,
    'd':14,
    'c':10,
    'b':6,
    'a':2
}


white = input()
white = white[7:].split(',')
black = input()
black = black[7:].split(',')

# print(white)
# print(black)
# exit()


def check_row(r):
    if r == '1':
        return row1
    elif r == '2':
        return row2
    elif r == '3':
        return row3
    elif r == '4':
        return row4
    elif r == '5':
        return row5
    elif r == '6':
        return row6
    elif r == '7':
        return row7
    elif r == '8':
        return row8

x = max(len(white),len(black))
for i in range(x):
    try:
        # White
        cur = white[i]
        if len(cur) == 2:
            row = check_row(cur[1])
            col = alph[cur[0]]
            row[col] = 'P'
        else:
            row = check_row(cur[2])
            col = alph[cur[1]]
            row[col] = cur[0]
        #print(white[i],black[i])
    except :
        pass

    try:
        cur = black[i]
        if len(cur) == 2:
            row = check_row(cur[1])
            col = alph[cur[0]]
            row[col] = 'p'
        else:
            row = check_row(cur[2])
            col = alph[cur[1]]
            row[col] = cur[0].lower()
    except IndexError:
        pass



print(norm_r)
print(''.join(row8))
print(norm_r)
print(''.join(row7))
print(norm_r)
print(''.join(row6))
print(norm_r)
print(''.join(row5))
print(norm_r)
print(''.join(row4))
print(norm_r)
print(''.join(row3))
print(norm_r)
print(''.join(row2))
print(norm_r)
print(''.join(row1))
print(norm_r)