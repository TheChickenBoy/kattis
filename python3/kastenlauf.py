class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge_between_vertex(self, x, y):
        self.edges[(x,y)] = set()

        for q,r in self.edges.keys():
            if x == q and y == r:
                continue
            elif abs(x-q)+abs(y-r) <= 1000: # Special case for a problem
                self.edges[(q,r)].add((x,y))
                self.edges[(x,y)].add((q,r))

    def is_connected(self, s_x, s_y, e_x, e_y):
        visited = set()
        stack = [(s_x,s_y)]

        while stack:
            x,y = stack.pop()
            if x == e_x and y == e_y:
                return True
            elif (x,y) in visited:
                continue
            else:
                visited.add((x,y))
                for q,r in self.edges[(x,y)]:
                    if (q,r) not in visited:
                        stack.append((q,r))
        return False

for i in range(int(input())):
    g = Graph()
    n = int(input())
    s_x,s_y = map(int,input().split())
    g.add_edge_between_vertex(s_x,s_y)

    for j in range(n):
        x,y = map(int,input().split())
        g.add_edge_between_vertex(x,y)
    
    e_x,e_y = map(int,input().split())
    g.add_edge_between_vertex(e_x,e_y)

    print("happy") if g.is_connected(s_x,s_y,e_x,e_y) else print("sad")