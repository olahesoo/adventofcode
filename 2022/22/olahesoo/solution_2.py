def turn(heading, direction):
    x, y = heading
    if direction == 'L':
        return (-y, x)
    elif direction == 'R':
        return (y, -x)
    return heading

with open('input') as infile:
    inlines = [i.rstrip() for i in infile.readlines()]

# My cube sections are arranged
#  12
#  3
# 45
# 6
section_side_length = len(inlines[-3])
section_bottom_left = {
        1: (section_side_length, section_side_length * 3),
        2: (section_side_length * 2, section_side_length * 3),
        3: (section_side_length, section_side_length * 2),
        4: (0, section_side_length) ,
        5: (section_side_length, section_side_length),
        6: (0, 0)
        }

def get_section(position):
    x, y = position
    if x < section_side_length:
        if y < section_side_length:
            return 6
        elif y < section_side_length * 2:
            return 4
    elif x < section_side_length * 2:
        assert y >= section_side_length, (position, section_side_length)
        if y < section_side_length * 2:
            return 5
        elif y < section_side_length * 3:
            return 3
        elif y < section_side_length * 4:
            return 1
    else:
        assert x < section_side_length * 3, (position, section_side_length)
        assert y >= section_side_length * 3, (position, section_side_length)
        assert y < section_side_length * 4, (position, section_side_length)
        return 2
    raise RuntimeError((position, section_side_length))

def global_to_section_pos(position):
    section = get_section(position)
    x, y = position
    ref_x, ref_y = section_bottom_left[section]
    return (x - ref_x, y - ref_y)

def section_to_global_pos(position, section):
    x, y = position
    ref_x, ref_y = section_bottom_left[section]
    return (x + ref_x, y + ref_y)

def switch_section(section_position, section, heading):
    x, y = section_position
    max_coord = section_side_length - 1
    assert 0 <= x < section_side_length, (section_position, section, heading)
    assert 0 <= y < section_side_length, (section_position, section, heading)
    if section == 1:
        if heading == (1, 0):
            return ((0, y), 2, (1, 0))
        elif heading == (0, 1):
            return ((0, max_coord - x), 6, (1, 0))
        elif heading == (-1, 0):
            return ((0, max_coord - y), 4, (1, 0))
        elif heading == (0, -1):
            return ((x, max_coord), 3, (0, -1))
    elif section == 2:
        if heading == (1, 0):
            return ((max_coord, max_coord - y), 5, (-1, 0))
        elif heading == (0, 1):
            return ((x, 0), 6, (0, 1))
        elif heading == (-1, 0):
            return ((max_coord, y), 1, (-1, 0))
        elif heading == (0, -1):
            return ((max_coord, max_coord - x), 3, (-1, 0))
    elif section == 3:
        if heading == (1, 0):
            return ((max_coord - y, 0), 2, (0, 1))
        elif heading == (0, 1):
            return ((x, 0), 1, (0, 1))
        elif heading == (-1, 0):
            return ((max_coord - y, max_coord), 4, (0, -1))
        elif heading == (0, -1):
            return ((x, max_coord), 5, (0, -1))
    elif section == 4:
        if heading == (1, 0):
            return ((0, y), 5, (1, 0))
        elif heading == (0, 1):
            return ((0, max_coord - x), 3, (1, 0))
        elif heading == (-1, 0):
            return ((0, max_coord - y), 1, (1, 0))
        elif heading == (0, -1):
            return ((x, max_coord), 6, (0, -1))
    elif section == 5:
        if heading == (1, 0):
            return ((max_coord, max_coord - y), 2, (-1, 0))
        elif heading == (0, 1):
            return ((x, 0), 3, (0, 1))
        elif heading == (-1, 0):
            return ((max_coord, y), 4, (-1, 0))
        elif heading == (0, -1):
            return ((max_coord, max_coord - x), 6, (-1, 0))
    elif section == 6:
        if heading == (1, 0):
            return ((max_coord - y, 0), 5, (0, 1))
        elif heading == (0, 1):
            return ((x, 0), 4, (0, 1))
        elif heading == (-1, 0):
            return ((max_coord - y, max_coord), 1, (0, -1))
        elif heading == (0, -1):
            return ((x, max_coord), 2, (0, -1))
    raise RuntimeError(section_position, section, heading)

def step(section_position, section, heading, board_map):
    x, y = section_position
    next_step = (x + heading[0], y + heading[1])
    next_x, next_y = next_step
    next_section, next_heading  = section, heading
    if next_x < 0 or next_x >= section_side_length or next_y < 0 or next_y >= section_side_length:
        next_step, next_section, next_heading = switch_section(section_position, section, heading)

    if board_map[section_to_global_pos(next_step, next_section)] == '#':
        return section_position, section, heading
    elif board_map[section_to_global_pos(next_step, next_section)] == '.':
        return next_step, next_section, next_heading
    else:
        raise RuntimeError((section_position, section, heading))

def follow_path(section_position, section, heading, distance, turn_direction, board_map):
    for i in range(distance):
        section_position, section, heading = step(section_position, section, heading, board_map)
    if turn_direction:
        heading = turn(heading, turn_direction)
    return (section_position, section, heading)

def test_moving(start_section_pos, start_section, start_heading, corner_faces):
    test_path_clockwise = [(1, 'R'), (1, 'R'), (1, 'R')]
    test_path_counterclockwise = [(0, 'R'), (1, 'L'), (1, 'L'), (1, 'L'), (0, 'L')]
    test_board_map = {}
    section_pos, section, heading = start_section_pos, start_section, start_heading
    test_board_map = {section_to_global_pos(*i): '.' for i in corner_faces}
    for i in test_path_clockwise:
        section_pos, section, heading = follow_path(section_pos, section, heading, *i, test_board_map)
    assert (start_section_pos, start_section, start_heading) == (section_pos, section, heading), (start_section_pos, start_section, start_heading)

    for i in test_path_counterclockwise:
        section_pos, section, heading = follow_path(section_pos, section, heading, *i, test_board_map)
    assert (start_section_pos, start_section, start_heading) == (section_pos, section, heading), (start_section_pos, start_section, start_heading)

test_moving((49, 0), 1, (1, 0), [((49, 0), 1), ((0, 0), 2), ((49, 49), 3)])
test_moving((49, 49), 1, (0, 1), [((49, 49), 1), ((0, 0), 6), ((0, 49), 2)])
test_moving((0, 49), 1, (-1, 0), [((0, 49), 1), ((0, 0), 4), ((0, 49), 6)])
test_moving((0, 0), 1, (0, -1), [((0, 0), 1), ((0, 49), 3), ((0, 49), 4)])

test_moving((0, 0), 5, (0, -1), [((0, 0), 5), ((49, 49), 6), ((49, 0), 4)])
test_moving((0, 49), 5, (-1, 0), [((0, 49), 5), ((49, 49), 4), ((0, 0), 3)])
test_moving((49, 49), 5, (0, 1), [((49, 49), 5), ((49, 0), 3), ((49, 0), 2)])
test_moving((49, 0), 5, (1, 0), [((49, 0), 5), ((49, 49), 2), ((49, 0), 6)])

board_map = {}
map_height = len(inlines[:-2])
for i in range(map_height):
    for j in range(len(inlines[i])):
        tile = inlines[i][j]
        if tile != ' ':
            board_map[(j, map_height-i-1)] = inlines[i][j]

sections = {
        1: {i for i in board_map if get_section(i) == 1},
        2: {i for i in board_map if get_section(i) == 2},
        3: {i for i in board_map if get_section(i) == 3},
        4: {i for i in board_map if get_section(i) == 4},
        5: {i for i in board_map if get_section(i) == 5},
        6: {i for i in board_map if get_section(i) == 6}
        }

for section in sections:
    for position in sections[section]:
        x, y = position
        ref_x, ref_y = section_bottom_left[section]
        assert ref_x <= x < ref_x + section_side_length, (section, position)
        assert ref_y <= y < ref_y + section_side_length, (section, position)

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
section_position = global_to_section_pos(position)
section = get_section(position)
for i in path:
    section_position, section, heading = follow_path(section_position, section, heading, *i, board_map)

heading_map = {
        (1, 0): 0,
        (0, -1): 1,
        (-1, 0): 2,
        (0, 1): 3
        }

x, y = section_to_global_pos(section_position, section)
answer = 1000 * (map_height - y) + 4 * (x + 1) + heading_map[heading]
print(answer)

