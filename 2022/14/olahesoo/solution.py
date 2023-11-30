def get_sand_rest_coords(rock_locations, abyss_depth,  drop_location):
    location = drop_location
    while True:
        x, y = location
        next_location = (x, y+1)
        if next_location in rock_locations:
            next_location = (x-1, y+1)
        if next_location in rock_locations:
            next_location = (x+1, y+1)
        if next_location in rock_locations:
            return location
        if y > abyss_depth:
            return False
        location = next_location

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

rock_locations = set()
for i in inlines:
    path = i.split(' -> ')
    x = int(path[0].split(',')[0])
    y = int(path[0].split(',')[1])
    for i in range(1, len(path)):
        next_x = int(path[i].split(',')[0])
        next_y = int(path[i].split(',')[1])
        if x == next_x:
            if y < next_y:
                for j in range(y, next_y + 1):
                    rock_locations.add((x, j))
                    y = next_y
            else:
                for j in range(y, next_y - 1, -1):
                    rock_locations.add((x, j))
                    y = next_y
        else:
            if x < next_x:
                for j in range(x, next_x + 1):
                    rock_locations.add((j, y))
                    x = next_x
            else:
                for j in range(x, next_x - 1, -1):
                    rock_locations.add((j, y))
                    x = next_x

abyss_depth = max([y for (x, y) in rock_locations])

sand_count = 0
sand_rest_coords = get_sand_rest_coords(rock_locations, abyss_depth, (500, 0))
while sand_rest_coords:
    rock_locations.add(sand_rest_coords)
    sand_count += 1
    sand_rest_coords = get_sand_rest_coords(rock_locations, abyss_depth, (500, 0))

print(sand_count)

