def complete_instruction(cycle_count, register_value, line):
    if line == 'noop':
        return (cycle_count + 1, register_value)
    else:
        return(cycle_count + 2, register_value + int(line.split(' ')[1]))

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

cycle_count = 0
register_value = 1
index = 0
output_sum = 0
drawn_pixels = []

while cycle_count < 240:
    next_cycle_count, next_register_value = complete_instruction(cycle_count, register_value, inlines[index])
    while cycle_count < next_cycle_count:
        cycle_count += 1
        pixel_location = (cycle_count - 1) % 40
        drawn_pixels.append('#' if abs(pixel_location - register_value) <= 1 else ' ')
    register_value = next_register_value
    index += 1

for i in range(0, 240, 40):
    print(''.join(drawn_pixels[i:i+40]))

