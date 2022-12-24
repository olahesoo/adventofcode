from collections import defaultdict
from dataclasses import dataclass, field
from queue import PriorityQueue

def move_blizzards_in_location(location, blizzards, max_x, max_y):
    x, y = location
    next_locations = []
    for blizzard in blizzards:
        if blizzard == '^':
            if y+1 > max_y:
                next_locations.append(((x, 0), blizzard))
            else:
                next_locations.append(((x, y+1), blizzard))
        elif blizzard == 'v':
            if y-1 < 0:
                next_locations.append(((x, max_y), blizzard))
            else:
                next_locations.append(((x, y-1), blizzard))
        elif blizzard == '<':
            if x-1 < 0:
                next_locations.append(((max_x, y), blizzard))
            else:
                next_locations.append(((x-1, y), blizzard))
        elif blizzard == '>':
            if x+1 > max_x:
                next_locations.append(((0, y), blizzard))
            else:
                next_locations.append(((x+1, y), blizzard))
        else:
            raise RuntimeError(blizzard)
    return next_locations

def move_all_blizzards(blizzards_map, max_x, max_y):
    next_blizzards_map = defaultdict(list)
    for location in blizzards_map:
        for next_location in move_blizzards_in_location(location, blizzards_map[location], max_x, max_y):
            blizzard_location, blizzard = next_location
            next_blizzards_map[blizzard_location].append(blizzard)
    return next_blizzards_map

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_shortest_path(location, blizzards_maps, step_count, max_x, max_y, start_location, end_location):
    if len(blizzards_maps) <= step_count:
        blizzards_maps.append(move_all_blizzards(blizzards_maps[-1], max_x, max_y))
    blizzards_map = blizzards_maps[step_count + 1]
    

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

blizzards_map = {}
max_y = len(inlines) - 3
max_x = len(inlines[0]) - 3
for col in range(max_x + 1):
    for row in range(max_y + 1):
        coords = (col, row)
        map_item = inlines[max_y - row + 1][col + 1] 
        if map_item != '.':
            blizzards_map[coords] = list(map_item)

blizzards_maps = [blizzards_map]
start_location = (0, max_y + 1)
end_location = (max_x, -1)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
highest_steps = 0

@dataclass(order=True)
class SearchLocation:
    location: (int, int) = field(compare=False)
    step_count: int = field(compare=False)
    priority: int = field(init=False)

    def __post_init__(self):
        x, y = self.location
        self.priority = self.step_count # + (abs(end_location[0] - x) + abs(end_location[1] - y))

search_start = SearchLocation(start_location, 0)
to_search = PriorityQueue()
to_search.put(search_start)
searched = set()
best_paths = defaultdict(list)

while True:
    searching = to_search.get()
    location, step_count = searching.location, searching.step_count
    if (location, step_count) in searched:
        continue
    if step_count > highest_steps:
        print(step_count)
        highest_steps = step_count
    required_map = step_count + 1
    if len(blizzards_maps) <= required_map:
        blizzards_maps.append(move_all_blizzards(blizzards_maps[-1], max_x, max_y))
    x, y = location
    blizzards_map = blizzards_maps[required_map]
    for direction in directions:
        next_x = x + direction[0]
        next_y = y + direction[1]
        if (next_x, next_y) == end_location:
            print(step_count + 1)
            exit()
        if 0 <= next_x <= max_x and 0 <= next_y <= max_y and (next_x, next_y) not in blizzards_map:
            next_location = (next_x, next_y)
            to_search.put(SearchLocation(next_location, step_count + 1))
            current_path = best_paths[location].copy()
            current_path.append((next_location, step_count + 1))
            best_paths[next_location] = current_path
        if location not in blizzards_map:
            to_search.put(SearchLocation(location, step_count + 1))
            best_paths[location].append((location, step_count + 1))
    searched.add((location, step_count))

