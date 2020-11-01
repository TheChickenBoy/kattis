def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

    
def GreedyTour(nodes, n):
    """
    2.8 points
    """
    tour = [0]*n
    #used[0] = True
    used = [False]*n
    used[0] = True
    for i in range(1,n):
        best = -1
        for j in range(0,n):
            if not used[j] and (best == -1 or dist(nodes[tour[i-1]],nodes[j]) < dist(nodes[tour[i-1]],nodes[best])):
                best = j
        tour[i] = best
        used[best] = True
    return tour

nodes = []
for i in range(int(input())):
    x,y = map(float,input().split())
    nodes.append((x,y))

t = GreedyTour(nodes,len(nodes))
for c in t:
    print(c)
