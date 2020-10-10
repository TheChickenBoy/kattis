for i in range(int(input())):
    l = list(map(int,input().split()))
    odd = even = a = 0
    for i in range(1,l[1]+1):
        a+=i
    for c,i in enumerate(range(1,l[1]*2+1,2)):
        if c<=l[1]:
            odd +=i
        else:
            break
    for c,i in enumerate(range(2,l[1]*2+1,2)):
        if c<=l[1]:
            even +=i
        else:
            break
        
    print(l[0],a,odd,even) 