import sys

info = input()
info = info.split()
m = []
for i in range(0,int(info[0])):
    m.append(input())

#print(*m)
n = int(input())

for l in sys.stdin:
    cords=l.split()
    print('Start: ('+cords[0]+','+cords[1]+')', 'Goal: ('+cords[2]+','+cords[3]+')')

    line = m[int(cords[0])-1]
    pos = line[int(cords[1])-1]
    gline = m[int(cords[2])-1]
    gpos = gline[int(cords[3])-1]

    if pos != gpos:
        print('neither')
        continue