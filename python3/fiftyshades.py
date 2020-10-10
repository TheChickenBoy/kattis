c=0
for i in range(int(input())):
    l = input()
    if "pink" in l.lower() or "rose" in l.lower():
        c+=1
print(c) if c > 0 else print("I must watch Star Wars with my daughter")