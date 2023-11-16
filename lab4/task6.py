def dfs(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0

    visited[row][col] = True
    diamonds_collected = 0

    if grid[row][col] == 'D':
        diamonds_collected = 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        diamonds_collected += dfs(grid, visited, row + dr, col + dc)

    return diamonds_collected


def max_diamonds(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    max_diamonds_collected = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                diamonds_collected = dfs(grid, visited, i, j)
                max_diamonds_collected = max(max_diamonds_collected, diamonds_collected)

    return max_diamonds_collected


#input output file
openfile = open("./input6_3.txt", "r")
readfile = openfile.readlines()
outputfile = open("./output6_3.txt", "w")

row, col = map(int, readfile[0].split())
data = readfile[1::]
grid = [line.strip() for line in data]

max_dia_collect = max_diamonds(grid)
# print(max_dia_collect)
outputfile.write(str(max_dia_collect)+"\n")