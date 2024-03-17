import itertools

def tsp_branch_and_bound(nodes, start):
    n = len(nodes)
    best_tour = None
    best_cost = float('inf')
    stack = [(start, [start], 0)]
    while stack:
        current_city, tour, cost = stack.pop()
        if len(tour) == n:
            if best_tour is None or cost < best_cost:
                best_tour = tour
                best_cost = cost
        for next_city in set(nodes) - set(tour):
            next_cost = cost + dist(nodes[current_city], nodes[next_city])
            if best_tour and next_cost >= best_cost:
                continue
            stack.append((next_city, tour + [next_city], next_cost))
    return best_tour

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

nodes = [(x,y) for x,y in zip(range(1000),range(1000))]
start = 0
best_tour = tsp_branch_and_bound(nodes, start)
print(best_tour)
