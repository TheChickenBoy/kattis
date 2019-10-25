a = 1
b = 0
r = True
for i in range(0,int(input())):
    if r:
        t = b+a
        a=b
        b=t
    else:
        a=b
print(a,b)
