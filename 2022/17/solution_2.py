from math import floor

def can_move_sideways(field, rock_position, direction, field_width):
    if direction == '<':
        for i in rock_position:
            if i[0] == 0 or (i[0] - 1, i[1]) in field:
                return False
    else:
        assert direction == '>'
        for i in rock_position:
            if i[0] == field_width - 1 or (i[0] + 1, i[1]) in field:
                return False
    return True

def can_move_down(field, rock_position):
    for i in rock_position:
        if (i[0], i[1] - 1) in field:
            return False
    return True

def cull_field(field, field_width):
    next_field = set()
    for i in range(field_width):
        highest_point = max(j[1] for j in field if j[0] == i)
        next_field.add((i, highest_point))
    return next_field

def move_step(field, rock_coords, direction, rock_index, stopped_rock_count, rock_formations, field_width=7):
    rock_position = set([((rock_coords[0] + i[0]) % field_width, rock_coords[1] + i[1]) for i in rock_formations[rock_index]])
    if can_move_sideways(field, rock_position, direction, field_width):
        if direction == '<':
            rock_coords = (rock_coords[0] - 1, rock_coords[1])
        else:
            assert direction == '>'
            rock_coords = (rock_coords[0] + 1, rock_coords[1])

    rock_position = set([((rock_coords[0] + i[0]) % field_width, rock_coords[1] + i[1]) for i in rock_formations[rock_index]])
    if can_move_down(field, rock_position):
        rock_coords = (rock_coords[0], rock_coords[1] - 1)
        return(field, rock_coords, rock_index, stopped_rock_count)
    else:
        stopped_rock_count += 1
        next_field =  field | rock_position
        return (next_field, (2, max([i[1] for i in next_field]) + 4), (rock_index + 1) % len(rock_formations), stopped_rock_count)

def get_highest_point(field):
    return max([i[1] for i in field])

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

rock_formations = [
        {(0, 0), (1, 0), (2, 0), (3, 0)},
        {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
        {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
        {(0, 0), (0, 1), (0, 2), (0, 3)},
        {(0, 0), (1, 0), (0, 1), (1, 1)}
    ]

field = set([(i, -1) for i in range(7)])
rock_coords = (2, 3)
jet_pattern = inlines[0]
jet_index = 0
rock_index = 0
stopped_rock_count = 0
target_stopped_rocks = 1000000000000

# Found by manual testing, might differ for your input
first_loop_top = 2720
first_loop_rocks = 1723
loop_top_delta = 2709
loop_rocks_delta = 1725

while stopped_rock_count < first_loop_rocks + loop_rocks_delta:
    field, rock_coords, rock_index, stopped_rock_count = move_step(field, rock_coords, jet_pattern[jet_index], rock_index, stopped_rock_count, rock_formations)
    jet_index = (jet_index + 1) % len(jet_pattern)
    if jet_index == 0:
        print(f'stopped rocks: {stopped_rock_count}')
        print(f'rock index: {rock_index}')
        print(f'highest point: {get_highest_point(field)}')

two_loops_highest_point = first_loop_top + loop_top_delta
remaining_rocks = target_stopped_rocks - stopped_rock_count
remaining_loops = floor(remaining_rocks / loop_rocks_delta)
highest_point = two_loops_highest_point + remaining_loops * loop_top_delta
remaining_rocks -= remaining_loops * loop_rocks_delta

stopped_rock_count = 0
while stopped_rock_count < remaining_rocks:
    field, rock_coords, rock_index, stopped_rock_count = move_step(field, rock_coords, jet_pattern[jet_index], rock_index, stopped_rock_count, rock_formations)
    jet_index = (jet_index + 1) % len(jet_pattern)

highest_point += max([i[1] for i in field]) + 1 - two_loops_highest_point

print(highest_point)

