n = int(input())
if n%2!=0:
    print("still running")
    exit()
s=0
for _ in range(0,n,2):
    a = int(input())
    b = int(input())
    s+= (b-a)

print(s)