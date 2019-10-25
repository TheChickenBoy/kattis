import sys

map = []

for i in range(0,4):
    l = input()
    map.append(l.split())

move = input()

if move == '0': #left
    for i in range(0,4):
        merge = ''
        for j in range(1,4):
            if map[i][j] == '0':
                continue
            if map[i][j-1] == '0':
                if j >= 2 and map[i][j-2] == '0':
                    if j == 3 and map[i][j-3] == '0':
                        map[i][j-3] = map[i][j]
                        map[i][j]='0'
                    elif map[i][j-3] == map[i][j] and  map[i][j]!=merge:
                        merge = str(int(map[i][j])*2)
                        map[i][j-3] = merge
                        map[i][j]='0'
                    elif map[i][j-2] == map[i][j] and map[i][j]!=merge:
                        merge = str(int(map[i][j])*2)
                        map[i][j-2] = merge
                        map[i][j]='0'
                    else:
                        map[i][j-2] = map[i][j]
                        map[i][j]='0'
                else:
                    if j >= 2 and map[i][j-2] == map[i][j] and map[i][j]!=merge:
                        merge = str(int(map[i][j])*2)
                        map[i][j-2] = merge
                        map[i][j]='0'
                    else:
                        map[i][j-1] = map[i][j]
                        map[i][j]='0'
            elif  map[i][j-1] == map[i][j] and map[i][j]!=merge:
                merge = str(int(map[i][j])*2)
                map[i][j-1] = merge
                map[i][j]='0'

elif move == '1': #up
    for i in range(0,4):

        merge = ''
        for j in range(1,4):
            if map[j][i] == '0':
                continue
            if map[j-1][i] == '0':
                if j >= 2 and map[j-2][i] == '0':
                    if j == 3 and map[j-3][i] == '0':
                        map[j-3][i] = map[j][i]
                        map[j][i]='0'
                    elif map[j-3][i] == map[j][i] and  map[j][i]!=merge:
                        merge = str(int(map[j][i])*2)
                        map[j-3][i] = merge
                        map[j][i]='0'
                    elif map[j-2][i] == map[j][i] and map[j][i]!=merge:
                        merge = str(int(map[j][i])*2)
                        map[j-2][i] = merge
                        map[j][i]='0'
                    else:
                        map[j-2][i] = map[j][i]
                        map[j][i]='0'
                else:
                    if j >= 2 and map[j-2][i] == map[j][i] and map[j][i]!=merge:
                        merge = str(int(map[j][i])*2)
                        map[j-2][i] = merge
                        map[j][i]='0'
                    else:
                        map[j-1][i] = map[j][i]
                        map[j][i]='0'
            elif  map[j-1][i] == map[j][i] and map[j][i]!=merge:
                merge = str(int(map[j][i])*2)
                map[j-1][i] = merge
                map[j][i]='0'

elif move == '2': #right
    for i in range(0,4):
        merge = ''
        for j in range(1,4):
            if map[i][3-j] == '0':
                continue
            if map[i][4-j] == map[i][3-j] and merge != map[i][3-j]:
                merge = str(int(map[i][3-j])*2)
                map[i][4-j] = merge
                map[i][3-j] = '0'
            elif map[i][4-j] == '0':
                if j>=2:
                    if map[i][5-j] == '0':
                        if map[i][6-j] == '0':
                            map[i][6-j] = map[i][3-j]
                            map[i][3-j] = '0'
                        elif map[i][6-j] == map[i][3-j] and  merge != map[i][3-j]:
                            merge = str(int(map[i][3-j])*2)
                            map[i][6-j] = merge
                            map[i][3-j] = '0'
                        else:
                            map[i][5-j] = map[i][3-j]
                            map[i][3-j] = '0'
                    else:
                        if map[i][5-j] == map[i][3-j] and merge != map[i][3-j]:
                            merge = str(int(map[i][3-j])*2)
                            map[i][5-j] = merge
                            map[i][3-j] = '0'
                        else:
                            map[i][4-j] = map[i][3-j]
                            map[i][3-j] = '0'
                else:
                    map[i][4-j] = map[i][3-j]
                    map[i][3-j] = '0'
else: #down
    for i in range(0,4):
        merge = ''
        for j in range(1,4):
            if map[3-j][i] == '0':
                continue
            if map[4-j][i] == map[3-j][i] and merge != map[3-j][i]:
                merge = str(int(map[3-j][i])*2)
                map[4-j][i] = merge
                map[3-j][i] = '0'
            elif map[4-j][i] == '0':
                if j>=2:
                    if map[5-j][i] == '0':
                        if map[6-j][i] == '0':
                            map[6-j][i] = map[3-j][i]
                            map[3-j][i] = '0'
                        elif map[6-j][i] == map[3-j][i] and  merge != map[3-j][i]:
                            merge = str(int(map[3-j][i])*2)
                            map[6-j][i] = merge
                            map[3-j][i] = '0'
                        else:
                            map[5-j][i] = map[3-j][i]
                            map[3-j][i] = '0'
                    else:
                        if map[5-j][i] == map[3-j][i] and merge != map[3-j][i]:
                            merge = str(int(map[3-j][i])*2)
                            map[5-j][i] = merge
                            map[3-j][i] = '0'
                        else:
                            map[4-j][i] = map[3-j][i]
                            map[3-j][i] = '0'
                else:
                    map[4-j][i] = map[3-j][i]
                    map[3-j][i] = '0'

for r in map:
    print(r[0] + " " +r[1] + " " +r[2] + " " +r[3])
