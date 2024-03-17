def count_burning_trees(N, M, T, burning_coords, chopped_coords):
    count = len(burning_coords)

    # Simulate the spread of fire for T minutes
    while T > 0:
        new_burning = set()
        for x, y in burning_coords:
            # Mark neighbors as burning if they are not chopped-down
            if (x-1, y) not in chopped_coords:
                new_burning.add((x-1, y))
                count += 1
            if (x+1, y) not in chopped_coords:
                new_burning.add((x+1, y))
                count += 1
            if (x, y-1) not in chopped_coords:
                new_burning.add((x, y-1))
                count += 1
            if (x, y+1) not in chopped_coords:
                new_burning.add((x, y+1))
                count += 1
        if not new_burning:
            break
        burning_coords = new_burning
        T -= 1
    # Count number of trees that are on fire
    return count

N,M,T = map(int,input().split())
burning_coords = set()
chopped_coords = set()
for _ in range(N):
    x,y = map(int,input().split())
    burning_coords.add((x, y))
for _ in range(M):
    x,y = map(int,input().split())
    chopped_coords.add((x, y))

print(count_burning_trees(N, M, T, burning_coords, chopped_coords))