from collections import defaultdict

def move_crates(crate_map, src, dest, amount):
    crate_map[dest] = crate_map[dest] + crate_map[src][-amount:]
    crate_map[src] = crate_map[src][:-amount]

with open('input') as infile:
    inlines = [i[:-1] for i in infile]

crate_amount = int((len(inlines[0]) + 1) / 4)
crate_map = defaultdict(list)

parse_crates_mode = True
for i in inlines:
    if i == '' or i[1] == '1':
        parse_crates_mode = False
        continue
    if parse_crates_mode:
        for j in range(crate_amount):
            crate = i[j*4 + 1]
            if crate != ' ':
                crate_map[j+1].insert(0, crate)
    else:
        move = i.split(' ')
        move_crates(crate_map, int(move[3]), int(move[5]), int(move[1]))

print(''.join([crate_map[i+1][-1] for i in range(crate_amount)]))

