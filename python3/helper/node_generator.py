import random

# Generate 1000 random nodes
n = 1000
nodes = [(random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(n)]

# Print the first 10 nodes
print(nodes[:10])

# Save the nodes to a file
with open(r"C:\Users\Gustav Wass\Documents\visualcode\kattis\python3\helper\test_nodes_1000.txt", "w") as f:
    f.write(f"{len(nodes)}\n")
    for node in nodes:
        f.write(f"{node[0]} {node[1]}\n")