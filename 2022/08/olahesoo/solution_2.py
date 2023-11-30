def calculate_scenic_score(coords, grid):
    x, y = coords
    tree_height = grid[x][y]
    scenic_score = 1
    view_distance = 0
    for i in range(y+1, len(grid)):
        view_distance += 1
        if grid[x][i] >= tree_height:
            break
    scenic_score *= view_distance
    view_distance = 0
    for i in range(y-1, -1, -1):
        view_distance += 1
        if grid[x][i] >= tree_height:
            break
    scenic_score *= view_distance
    view_distance = 0
    for i in range(x+1, len(grid)):
        view_distance += 1
        if grid[i][y] >= tree_height:
            break
    scenic_score *= view_distance
    view_distance = 0
    for i in range(x-1, -1, -1):
        view_distance += 1
        if grid[i][y] >= tree_height:
            break
    scenic_score *= view_distance
    return scenic_score

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

grid = []
for i in inlines:
    grid.append([int(tree) for tree in list(i)])

max_scenic_score = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        max_scenic_score = max(max_scenic_score, calculate_scenic_score((i, j), grid))

print(max_scenic_score)

