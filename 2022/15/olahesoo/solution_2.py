def add_line(new_line, lines_array):
    new_line = (min(new_line), max(new_line))
    new_lines_array = []
    to_process = new_line
    was_inserted = False
    for line in lines_array:
        if to_process[0] > line[1] + 1:
            if not was_inserted:
                new_lines_array.append(to_process)
                was_inserted = True
            new_lines_array.append(line)
        elif to_process[1] < line[0] - 1:
            new_lines_array.append(line)
        else:
            to_process = (min(*to_process, *line), max(*to_process, *line))
    if not was_inserted:
        new_lines_array.append(to_process)
    return new_lines_array

def beacon_free_coverage(row, scanners):
    coverage_lines = []
    for scanner in scanners:
        scanner_distance = abs(scanner[1] - row)
        beacon_distance = abs(scanner[0] - scanner[2]) + abs(scanner[1] - scanner[3])
        if scanner_distance > beacon_distance:
            continue
        else:
            distance_diff = beacon_distance - scanner_distance
            coverage_line = (scanner[0] - distance_diff, scanner[0] + distance_diff)
        coverage_lines = add_line(coverage_line, coverage_lines)
    scanners_in_row = set([i[0] for i in scanners if i[1] == row])
    beacons_in_row = set([i[2] for i in scanners if i[3] == row])
    objects_in_row = scanners_in_row.union(beacons_in_row)
    for i in objects_in_row:
        add_line([i, i], coverage_lines)
    return coverage_lines

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

scanners = []
for i in inlines:
    line = i.split(' ')
    scanners.append((int(line[2][2:-1]), int(line[3][2:-1]), int(line[8][2:-1]), int(line[9][2:])))

beacon_min = 0
beacon_max = 4000000
for i in range(beacon_max):
    if i % 10000 == 0:
        print(i)
    coverage = beacon_free_coverage(i, scanners)
    coverage = sorted([line for line in coverage if line[0] <= beacon_max and line[1] >= beacon_min])
    if len(coverage) > 1:
        print(coverage)
        print(i + (coverage[0][1] + 1) * 4000000)
        break

