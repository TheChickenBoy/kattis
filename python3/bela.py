import sys

info = input()
info = info.split()
dom = info[1]

score = 0
for l in sys.stdin:
    if 'A' in l:
        score+=11
        #continue
    elif 'K' in l:
        score+=4
    elif 'Q' in l:
        score+=3
    elif 'T' in l:
        score+=10
    elif '8' in l or '7' in l:
        continue
    elif '9' in l:
        if dom in l:
            score+=14
        else:
            continue
    elif 'J' in l:
        if dom in l:
            score+=20
        else:
            score+=2

print(score)
