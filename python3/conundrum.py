d = 0
for i,l in enumerate(input()):
    #print("i:",i,"l:",l)
    if l == 'P' and (i+1)%3 == 1:
        continue
    elif l == 'E' and (i+1)%3 == 2:
        continue
    elif l == 'R' and (i+1)%3 == 0:
        continue
    d+=1
print(d)