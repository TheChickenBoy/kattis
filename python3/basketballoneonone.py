a_score = 0
b_score = 0

l = input()

for i,c  in enumerate(l):
    if c == 'A':
        a_score += int(l[i+1])
    elif c == 'B':
        b_score += int(l[i+1])
    
    if a_score >= 11 or b_score >= 11:
        if abs(a_score-b_score) >= 2:
            print('A') if a_score > b_score else print('B')
            exit()