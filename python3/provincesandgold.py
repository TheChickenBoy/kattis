n = list(map(int,input().split()))
t = n[0]*3+n[1]*2+n[2]
s=''
if t >= 8:
    s = "Province or "
elif t >= 5:
    s = "Duchy or "
elif t >= 2:
    s = "Estate or "

if t >= 6:
    s += "Gold"
elif t >= 3:
    s += "Silver"
else:
    s += "Copper"
print(s)
