class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge_between_vertex(self, x, y):
        if x in self.edges:
            self.edges[x].add(y)   
        else:
            self.edges[x] = set()
            self.edges[x].add(x)
            self.edges[x].add(y)
        
        if y in self.edges:
            self.edges[y].add(x)
        else:
            self.edges[y] = set()
            self.edges[y].add(y)
            self.edges[y].add(x)
        
        for q in self.edges.keys():
            if q == x or q == y:
                continue
            if x in self.edges[q]:
                self.edges[x].add(q)
                self.edges[y].add(q)

    """
    3
    Fred Barney
    Betty Wilma
    Barney Betty
    """

    def nr_of_connections(self,s1,s2):
        #print(self.edges)
        return max(len(self.edges[s1]),len(self.edges[s2]))

g = Graph()
for i in range(int(input())):
    h1,h2 = input().split()
    g.add_edge_between_vertex(h1,h2)
    print(g.nr_of_connections(h1,h2))


# import itertools 
# graph = {}
# number = 0
# unreached = []

# # class Node(object):
# #     def __init__(self, v):
# #         self.value = v
# #         self.visited = False
# #     def set_visited(self):
# #         self.visited = True
# #     def set_unvisited(self):
# #         self.visited = False

# def find_isolated_nodes(g, i,s1,s2):
#     """ returns a list of isolated nodes. """
#     count = 0
#     visited = []
   
#     for key, value in g.items():
#         #print(key, value)
#         if value[0] == i:
#             value[0] += 1
#             if (s1 in value or s2 in value) or (s1 == key or s2 == key):
#             #new = g.get(key)
#                 if value[0] == i:
#                     continue
#                 for elm in value[1:]:
#                     #print("lol:",graph[elm][0])
#                     if graph[elm][0] <= i:
#                         count += 1
#                     #print("reached:",key, "with:",value)
                
#             # if s1 in value:
#             #     count += 1
#             # if s2 in value:
#             #     count += 1
#         #if not graph[node]:
#         #    count += 1
#     #print(g)
#     return count


# for i in range(int(input())):
#     n = input().split()
#     if n[0] in graph:
#         graph[n[0]].append(n[1])
#         if n[1] in graph:
#             graph[n[1]].append(n[0])
#         else:
#             number += 1
#             graph[n[1]] = [i,n[0]]
#     else:
#         graph[n[0]] = [i,n[1]]
#         graph[n[1]] = [i,n[0]]
#         number += 2
#     print(find_isolated_nodes(graph, i, n[0], n[1])+1)
#     #print(number-find_isolated_nodes(graph))

#     # if n[0] not in itertools.chain(*graph):
#     #     number += 1
#     # if n[1] not in itertools.chain(*graph):
#     #     number += 1
#     # graph.append((n[0],n[1]))
# #print(graph)
# #print(number)
