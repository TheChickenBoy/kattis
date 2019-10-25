for i in range(0,int(input())):
    a,b,c = map(int,input().split())
    if a+b == c or max(a,b)-min(a,b) == c or max(a,b)/min(a,b) == c or a*b == c:
        print("Possible")
    else:
        print("Impossible")
