import sys, math
for i,l in enumerate(sys.stdin):
    x,y,r = map(float,l.split())
    c = x + y*1j
    q=0
    z = 0
    while abs(z) < 2 and q < r:
        z = (z*z) + c
        q+=1
    if abs(z) < 2 :
        print("Case " + str(i+1)+": IN")
    else:
        print("Case "+str(i+1)+": OUT")
