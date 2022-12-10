def complete_instruction(cycle_count, register_value, line):
    if line == 'noop':
        return (cycle_count + 1, register_value)
    else:
        return(cycle_count + 2, register_value + int(line.split(' ')[1]))

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

answer_cycles = [20, 60, 100, 140, 180, 220]

cycle_count = 0
register_value = 1
index = 0
output_sum = 0

for cycle in answer_cycles:
    while cycle_count < cycle:
        next_cycle_count, next_register_value = complete_instruction(cycle_count, register_value, inlines[index])
        if next_cycle_count >= cycle:
            #print(f'adding {cycle} * {register_value}')
            output_sum += cycle * register_value
        cycle_count, register_value = next_cycle_count, next_register_value
        index += 1
        #print (cycle_count, register_value)

print(output_sum)

