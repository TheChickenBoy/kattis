# 1: 1
# 2: 10
# 3: 35
# 4: 84

def rec(i, x, sum):
    x+=2
    t = x*x
    if t+sum > goal:
        print(i)
        exit()
    else:
        i+=1
        rec(i,x,t+sum)

i=1
x=1
goal = int(input())
if goal < 10:
    print(1)
    exit()
rec(i,x,1)


