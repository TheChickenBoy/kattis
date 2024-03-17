import random

class KdNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

class KdTree:
    def __init__(self, data):
        self.k = len(data[0])
        self.root = self._build_tree(data, 0)

    def _build_tree(self, data, depth):
        if not data:
            return None
        axis = depth % self.k
        data.sort(key=lambda x: x[axis])
        median = len(data) // 2
        return KdNode(
            data[median],
            axis,
            left=self._build_tree(data[:median], depth+1),
            right=self._build_tree(data[median+1:], depth+1),
        )

    def _dist(self, a, b):
        """
        Euclidean distance between two points
        """
        return sum((x1 - x2) ** 2 for x1, x2 in zip(a, b))

    def _query_ball_point(self, node, point, r, depth, found):
        """
        Recursive function to search for points in the tree
        """
        if node is None:
            return
        if self._dist(node.point, point) <= r ** 2:
            found.append(node.point)
        axis = depth % self.k
        if point[axis] - r <= node.point[axis]:
            self._query_ball_point(node.left, point, r, depth + 1, found)
        if point[axis] + r >= node.point[axis]:
            self._query_ball_point(node.right, point, r, depth + 1, found)

    def query_ball_point(self, point, r):
        """
        Returns all points within a distance r from the given point
        """
        found = []
        self._query_ball_point(self.root, point, r, 0, found)
        return found


def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def nearest_neighbor_kdtree(nodes, n):
    tour = [0]
    used = [True] + [False]*(n-1)
    for i in range(1,n):
        best = -1
        for j in range(n):
            if not used[j] and (best == -1 or dist(nodes[tour[i-1]], nodes[j]) < dist(nodes[tour[i-1]], nodes[best])):
                best = j
        tour.append(best)
        used[best] = True
    return tour


def generate_neighbor(tour):
    n = len(tour)
    if n == 1:
        return tour
    while True:
        i, j = sorted(random.sample(range(n), 2))
        if i != j:
            break
    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
    return new_tour

def two_opt_swap(tour, i, j):
    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
    return new_tour

def tabu_search(nodes, n, max_iterations=1000, tabu_list_size=20, k_max=10):
    current_tour = nearest_neighbor_kdtree(nodes, n)
    best_tour = current_tour.copy()
    tabu_list = []
    for i in range(max_iterations):
        for j in range(n):
            if j not in tabu_list:
                neighbor = generate_neighbor(current_tour)
                if len(set(current_tour)) == n:
                    break
                if len(set(neighbor)) == n:
                    best_tour = neighbor
                    current_tour = neighbor.copy()
                else:
                    if len(tabu_list) >= tabu_list_size:
                        tabu_list.pop(0)
                    tabu_list.append(j)
    return best_tour



n = int(input())
nodes = []
for i in range(n):
    x,y = map(float,input().split())
    nodes.append((x,y))


t = tabu_search(nodes, n, max_iterations=10, tabu_list_size=5, k_max=1)
for c in t:
    print(c)