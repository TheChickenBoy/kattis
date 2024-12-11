r = 0
rn = ""
for i in range(int(input())):
    n, s = input().split()
    if r < int(s):
        r = int(s)
        rn = n
print(rn)