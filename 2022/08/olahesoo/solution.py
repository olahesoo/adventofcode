def line_coords_generator(grid):
    for i in range(len(grid)):
        yield([(i, j) for j in range(len(grid))])
        yield([(i, -j-1) for j in range(len(grid))])
        yield([(j, i) for j in range(len(grid))])
        yield([(-j-1, i) for j in range(len(grid))])

def count_trees(line_coords, grid):
    vis_line = []
    max_height = -1
    count = 0
    for coords in line_coords:
        x, y = coords
        tree_height = grid[x][y]
        if tree_height > max_height:
            vis_line.append(1)
            max_height = tree_height
        else:
            vis_line.append(0)
    return vis_line

def fill_visibility_map(line_coords, vis_map, grid):
    trees = count_trees(line_coords, grid)
    index = 0
    for coords in line_coords:
        x, y = coords
        if trees[index]:
            vis_map[x][y] = 1
        index += 1

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

grid = []
for i in inlines:
    grid.append([int(tree) for tree in list(i)])

visibility_map = []
for i in range(len(grid)):
    visibility_map.append([0]*len(grid))

for line_coords in line_coords_generator(grid):
    fill_visibility_map(line_coords, visibility_map, grid)

tree_count = 0
for i in visibility_map:
    for j in i:
        tree_count += j

print(tree_count)

