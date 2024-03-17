s = input().split()
o = []

for w in s:
    tc = ''
    wo = ''
    for c in w:
        if tc=='' or tc != c:
            tc = c
            wo += c
            continue
        elif tc == c:
            continue
    o.append(wo)
print(*o)