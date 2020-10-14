import itertools 
graph = {}
number = 0
unreached = []

# class Node(object):
#     def __init__(self, v):
#         self.value = v
#         self.visited = False
#     def set_visited(self):
#         self.visited = True
#     def set_unvisited(self):
#         self.visited = False

def find_isolated_nodes(g, i,s1,s2):
    """ returns a list of isolated nodes. """
    count = 0
    visited = []
   
    for key, value in g.items():
        #print(key, value)
        if value[0] == i:
            value[0] += 1
            if (s1 in value or s2 in value) or (s1 == key or s2 == key):
            #new = g.get(key)
                if value[0] == i:
                    continue
                for elm in value[1:]:
                    #print("lol:",graph[elm][0])
                    if graph[elm][0] <= i:
                        count += 1
                    #print("reached:",key, "with:",value)
                
            # if s1 in value:
            #     count += 1
            # if s2 in value:
            #     count += 1
        #if not graph[node]:
        #    count += 1
    #print(g)
    return count


for i in range(int(input())):
    n = input().split()
    if n[0] in graph:
        graph[n[0]].append(n[1])
        if n[1] in graph:
            graph[n[1]].append(n[0])
        else:
            number += 1
            graph[n[1]] = [i,n[0]]
    else:
        graph[n[0]] = [i,n[1]]
        graph[n[1]] = [i,n[0]]
        number += 2
    print(find_isolated_nodes(graph, i, n[0], n[1])+1)
    #print(number-find_isolated_nodes(graph))

    # if n[0] not in itertools.chain(*graph):
    #     number += 1
    # if n[1] not in itertools.chain(*graph):
    #     number += 1
    # graph.append((n[0],n[1]))
#print(graph)
#print(number)

