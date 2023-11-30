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

uncovered_sides = 0
for i in lava_coords:
    for j in directions:
        if (i[0]+j[0], i[1]+j[1], i[2]+j[2]) not in lava_coords:
            uncovered_sides += 1

print(uncovered_sides)

