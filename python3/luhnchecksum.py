for i in range(0,int(input())):
    l = input()
    x = 0
    sum = 0
    for j in range(len(l)-1,-1,-1):
        if x%2 != 0:
            t = int(l[j])*2
            if t > 9:
                s = str(t)
                t -= 9
            sum+=t
        else:
            sum+=int(l[j])
        x+=1
    print("PASS") if sum%10==0 else print("FAIL")
