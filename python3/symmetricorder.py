n = int(input())
x = 1
while n!=0:
    s = []
    for i in range(0,n):
        s.append(input())
    ss = sorted(s,key=len)
    print("SET "+str(x))
    if n%2 == 0:
        for j in range(0,len(ss),2):
            print(ss[j])
        for j in range(len(ss)-1,0,-2):
            print(ss[j])
    else:
        for j in range(0,len(ss),2):
            print(ss[j])
        for j in range(len(ss)-2,0,-2):
            print(ss[j])
    x+=1
    n = int(input())
