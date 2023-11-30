def turn(heading, direction):
    x, y = heading
    if direction == 'L':
        return (-y, x)
    elif direction == 'R':
        return (y, -x)
    return heading

def step(heading, position, board_map):
    x, y = position
    next_step = (x + heading[0], y + heading[1])
    if next_step not in board_map:
        if heading[0] == 1:
            next_step = (min([i[0] for i in board_map if i[1] == y]), y)
        elif heading[0] == -1:
            next_step = (max([i[0] for i in board_map if i[1] == y]), y)
        elif heading[1] == 1:
            next_step = (x, min([i[1] for i in board_map if i[0] == x]))
        elif heading[1] == -1:
            next_step = (x, max([i[1] for i in board_map if i[0] == x]))
        else:
            raise RuntimeError()
    if board_map[next_step] == '#':
        return position
    elif board_map[next_step] == '.':
        return next_step
    else:
        raise RuntimeError()

def follow_path(position, heading, distance, turn_direction, board_map):
    for i in range(distance):
        position = step(heading, position, board_map)
    if turn_direction:
        heading = turn(heading, turn_direction)
    return (position, heading)

with open('input') as infile:
    inlines = [i.rstrip() for i in infile.readlines()]

board_map = {}
map_height = len(inlines[:-2])
for i in range(map_height):
    for j in range(len(inlines[i])):
        tile = inlines[i][j]
        if tile != ' ':
            board_map[(j, map_height-i-1)] = inlines[i][j]

path_str = inlines[-1]
index = 0
number_acc = []
path = []
for i in path_str:
    if i == 'L' or i == 'R':
        path.append((int(''.join(number_acc)), i))
        number_acc = []
    else:
        number_acc.append(i)
path.append((int(''.join(number_acc)), None))

position = (min([i[0] for i in board_map if i[1] == map_height-1]), map_height-1)
heading = (1, 0)
for i in path:
    position, heading = follow_path(position, heading, *i, board_map)

heading_map = {
        (1, 0): 0,
        (0, -1): 1,
        (-1, 0): 2,
        (0, 1): 3
        }

x, y = position
answer = 1000 * (map_height - y) + 4 * (x + 1) + heading_map[heading]
print(answer)

