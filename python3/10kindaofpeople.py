import sys
import heapq

def floodfill(x, y):
    unvisited = []
    heapq.heappush(unvisited, (x, y))
    while unvisited:
        pos = heapq.heappop(unvisited)
        x, y = pos[0], pos[1]
        if m[x][y] == sp:
            m[x][y] = other
            if x > 0 and m[x-1][y] == sp:
                heapq.heappush(unvisited, (x-1, y))
            if y > 0 and m[x][y-1] == sp:
                heapq.heappush(unvisited, (x, y-1))
            if y < c - 1 and m[x][y+1] == sp:
                heapq.heappush(unvisited, (x, y+1))
            if x < r - 1 and m[x+1][y] == sp:
                heapq.heappush(unvisited, (x+1, y))

def check(x, y):
    if x == y:
        if d[x] == "1":
            print("decimal")
        else:
            print("binary")
    else:
        print("neither")

r, c = [int(x) for x in sys.stdin.readline().split()]
m = [0]*r
for i in range(r):
    l = list(sys.stdin.readline().strip())
    m[i] = l
other = 0
d = {}

for _ in range(int(sys.stdin.readline())):
    x1, y1, x2, y2 = [int(x) - 1 for x in sys.stdin.readline().split()]
    sp = m[x1][y1]
    gp = m[x2][y2]
    if type(sp) == int or type(gp) == int or sp != gp:
        check(sp, gp)
    else:
        other += 1
        d[other] = sp
        floodfill(x1, y1)
        check(m[x1][y1], m[x2][y2])