def get_sign(integer):
    if integer > 0:
        return 1
    elif integer == 0:
        return 0
    else:
        return -1

def balance_tail(head_pos, tail_pos):
    new_tail_pos = []
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        new_tail_pos.append(tail_x + get_sign(x_diff))
        new_tail_pos.append(tail_y + get_sign(y_diff))
    else:
        new_tail_pos = tail_pos
    return tuple(new_tail_pos)

def move_head(head_pos, tail_pos, direction, distance, tail_locations):
    for i in range(distance):
        head_pos = (head_pos[0] + direction[0], head_pos[1] + direction[1])
        tail_pos = balance_tail(head_pos, tail_pos)
        tail_locations.add(tail_pos)
    return head_pos, tail_pos, tail_locations

with open('input') as infile:
    inlines = [i.strip() for i in infile]

directions = {
        'R': (1, 0),
        'U': (0, 1),
        'L': (-1, 0),
        'D': (0, -1)
        }

head_pos = (0, 0)
tail_pos = (0, 0)
tail_locations = set()
tail_locations.add(tail_pos)

for i in inlines:
    direction, distance = i.split(' ')
    distance = int(distance)
    head_pos, tail_pos, tail_locations = move_head(head_pos, tail_pos, directions[direction], distance, tail_locations)

print(len(tail_locations))

