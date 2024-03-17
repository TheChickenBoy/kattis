n,p,s =  input().split()

for _ in range(int(s)):
    i = input().split()
    print("KEEP") if p in i[1:] else print("REMOVE")
