def count_parking_spaces(grid):
    rows = len(grid)
    cols = len(grid[0])
    parking_spaces = [0]*5
    for row in range(rows - 1):
        for col in range(cols - 1):
            if grid[row][col] != "#" and grid[row][col+1] != "#" and grid[row+1][col] != "#" and grid[row+1][col+1] != "#":
                if "X" not in grid[row][col] + grid[row][col+1] + grid[row+1][col] + grid[row+1][col+1]:
                    parking_spaces[0] += 1
                else:
                    count = 0
                    if grid[row][col] == "X":
                        count += 1
                    if grid[row][col+1] == "X":
                        count += 1
                    if grid[row+1][col] == "X":
                        count += 1
                    if grid[row+1][col+1] == "X":
                        count += 1
                    parking_spaces[count] += 1
    print("\n".join(str(p) for p in parking_spaces))

r,c = map(int, input().split())
grid = [input() for _ in range(r)]
count_parking_spaces(grid)
