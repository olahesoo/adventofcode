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

def balance_rope(rope):
    for i in range(len(rope) - 1):
        head = rope[i]
        tail = rope[i + 1]
        new_tail = balance_tail(head, tail)
        rope[i + 1] = new_tail
    return rope

def move_head(rope, direction, distance, tail_locations):
    for i in range(distance):
        rope[0] = (rope[0][0] + direction[0], rope[0][1] + direction[1])
        rope = balance_rope(rope)
        tail_locations.add(rope[-1])
    return rope, tail_locations

with open('input') as infile:
    inlines = [i.strip() for i in infile]

directions = {
        'R': (1, 0),
        'U': (0, 1),
        'L': (-1, 0),
        'D': (0, -1)
        }

rope = [(0, 0)]*10
tail_locations = set()
tail_locations.add(rope[-1])

for i in inlines:
    direction, distance = i.split(' ')
    distance = int(distance)
    rope, tail_locations = move_head(rope, directions[direction], distance, tail_locations)

print(len(tail_locations))

