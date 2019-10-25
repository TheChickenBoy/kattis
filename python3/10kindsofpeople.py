import sys

info = input()
info = info.split()
map = []
for i in range(0,int(info[0])):
    map.append(input())

#print(*map)
n = int(input())

for l in sys.stdin:
    cords=l.split()
    print('Start: ('+cords[0]+','+cords[1]+')', 'Goal: ('+cords[2]+','+cords[3]+')')

    line = map[int(cords[0])-1]
    pos = line[int(cords[1])-1]
    gline = map[int(cords[2])-1]
    gpos = gline[int(cords[3])-1]

    if pos != gpos:
        print('neither')
        continue
