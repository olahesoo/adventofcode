def get_valid_steps(coord, height_map, max_height_diff):
    output = []
    x, y = coord
    height = height_map[x][y]
    if x > 0 and height_map[x-1][y] - height <= 1:
        output.append((x-1, y))
    if x < len(height_map) - 1 and height_map[x+1][y] - height <= 1:
        output.append((x+1, y))
    if y > 0 and height_map[x][y-1] - height <= 1:
        output.append((x, y-1))
    if y < len(height_map[0]) - 1 and height_map[x][y+1] - height <= 1:
        output.append((x, y+1))

    return output

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

for i in range(len(inlines)):
    for j in range(len(inlines[i])):
        if inlines[i][j] == 'S':
            start_coord = (i, j)
        if inlines[i][j] == 'E':
            end_coord = (i, j)

height_map = []
for i in inlines:
    height_map.append([ord(letter) for letter in i])

height_map[start_coord[0]][start_coord[1]] = ord('a')
height_map[end_coord[0]][end_coord[1]] = ord('z')

to_search = []
distances = {}

for i in range(len(height_map)):
    for j in range(len(height_map[0])):
        if height_map[i][j] == ord('a'):
            to_search.append((i, j))
            distances[(i, j)] = 0

while to_search:
    searching = to_search.pop(0)
    distance = distances[searching]
    for coord in get_valid_steps(searching, height_map, 1):
        if not coord in distances or distances[coord] > distance + 1:
            distances[coord] = distance + 1
            to_search.append(coord)

print(distances[end_coord])

