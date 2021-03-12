x = int(input())
l = map(int,input().split())
l = sorted(l)

def ranges(nums):
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))

out = []
for r in ranges(l):
    if r[0] == r[1]:
        out.append(str(r[0]))
    elif r[0] == r[1]-1:
        out.append(str(r[0]))
        out.append(str(r[1]))
    else:
        out.append(str(r[0]) + "-" + str(r[1]))

print(*out)
