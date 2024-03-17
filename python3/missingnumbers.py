ln = []

for _ in range(int(input())):
    ln.append(int(input()))
l = list(range(1,ln[-1]))

s = list(set(l) - set(ln))
if not s:
    print("good job")
else:
    s.sort()
    for o in s:
        print(o)