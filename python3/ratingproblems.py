def average(lst):
    return sum(lst) / len(lst)

n,k = map(int,input().split())
scores = []
for _ in range(0,k):
    scores.append(float(input()))

if n == k:
    m = average(scores)
    print(m,m)
    exit()
else:
    high = []
    low = []
    for _ in range(0,n-k):
        high.append(3)
        low.append(-3)
    print(average(low+scores), average(high+scores))
