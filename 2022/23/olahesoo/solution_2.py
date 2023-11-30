from collections import defaultdict

moves = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
        }

def check_around(location, elves_map):
    x, y = location
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) == (x, y):
                continue
            if (i, j) in elves_map:
                return False
    return True

def propose_move(location, elves_map, priorities):
    if check_around(location, elves_map):
        return None
    x, y = location
    for move in priorities:
        free_spaces = True
        if move == 'N':
            for i in range(-1, 2):
                if (x+i, y+1) in elves_map:
                    break
            else:
                return (x, y+1)
        elif move == 'S':
            for i in range(-1, 2):
                if (x+i, y-1) in elves_map:
                    break
            else:
                return (x, y-1)
        elif move == 'E':
            for i in range(-1, 2):
                if (x+1, y+i) in elves_map:
                    break
            else:
                return (x+1, y)
        elif move == 'W':
            for i in range(-1, 2):
                if (x-1, y+i) in elves_map:
                    break
            else:
                return (x-1, y)
        else:
            raise RuntimeError(move)
    return None

def collect_proposed_moves(elves_map, priorities):
    proposed_moves = defaultdict(set)
    for i in elves_map:
        proposal = propose_move(i, elves_map, priorities)
        if proposal:
            proposed_moves[proposal].add(i)
    return proposed_moves

def step(elves_map, priorities):
    proposals = collect_proposed_moves(elves_map, priorities)

    next_elves_map = elves_map.copy()
    for (location, elves) in proposals.items():
        if len(elves) == 1:
            next_elves_map.add(location)
            next_elves_map.remove(elves.pop())

    next_priorities = priorities.copy()
    first_priority = next_priorities.pop(0)
    next_priorities.append(first_priority)

    to_continue = len(proposals) > 0

    return next_elves_map, next_priorities, to_continue

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

map_height = len(inlines)
elves_map = set()
for row in range(map_height):
    for col in range(len(inlines[row])):
        if inlines[row][col] == '#':
            elves_map.add((col,map_height - row - 1))

priorities = ['N', 'S', 'W', 'E']
to_continue = True
round_count = 0

while to_continue:
    round_count += 1
    elves_map, priorities, to_continue = step(elves_map, priorities)

elves_x = {i[0] for i in elves_map}
elves_y = {i[1] for i in elves_map}

print(round_count)

