with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

directions = [
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0)
        ]

lava_coords = set()
for i in inlines:
    x, y, z = i.split(',')
    lava_coords.add((int(x), int(y), int(z)))

min_x = min([i[0] for i in lava_coords])
max_x = max([i[0] for i in lava_coords])
min_y = min([i[1] for i in lava_coords])
max_y = max([i[1] for i in lava_coords])
min_z = min([i[2] for i in lava_coords])
max_z = max([i[2] for i in lava_coords])

steam_filled = set()
to_fill = [(min_x - 1, min_y - 1, min_z - 1)]

while to_fill:
    filling = to_fill.pop(0)
    steam_filled.add(filling)
    for i in directions:
        checking = (filling[0]+i[0], filling[1]+i[1], filling[2]+i[2])
        if checking not in lava_coords and checking not in steam_filled and checking not in to_fill and checking[0] >= min_x - 1 and checking[0] <= max_x + 1 and checking[1] >= min_y - 1 and checking[1] <= max_y + 1 and checking[2] >= min_z - 1 and checking[2] <= max_z + 1:
            to_fill.append(checking)

uncovered_sides = 0
for i in steam_filled:
    for j in directions:
        if (i[0]+j[0], i[1]+j[1], i[2]+j[2]) in lava_coords:
            uncovered_sides += 1

print(uncovered_sides)

