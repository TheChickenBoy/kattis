l = []
check = 0
for i in range(int(input())):
    s = input()
    l.append(s)
    if(i==0):
        continue
    if s[0] == l[i-1][0]:
        for j, c in enumerate(s):
            if j == len(l[i-1]):
                break
            elif c == l[i-1][j]:
                continue
            elif c < l[i-1][j]:
                if check == 0 or check == -1:
                    #print(s,check)
                    check = -1
                    break
                else:
                    print("NEITHER")
                    exit()
            else:
                if check == 0 or check == 1:
                    check = 1
                    break
                else:
                    #print(c,"och",l[i-1][j])
                    print("NEITHER")
                    exit()
    elif s[0] < l[i-1][0]:
        if check == 0 or check == -1:
            check = -1
            continue
        else:
            print("NEITHER")
            exit()
    else:
        if check == 0 or check == 1:
            check = 1
            continue
        else:
            print("NEITHER")
            exit()

if check == 1: 
    print("INCREASING") 
elif check == -1:
     print("DECREASING")
else:
    print("NEITHER")
