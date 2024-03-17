k,m,n = map(int, input().split())
player = True
while k>m:
    player = not player
    if k>n:
        k-=n
    elif k>=m:
        k-=k

if player:
    print("Barb")
else:
    print("Alex")