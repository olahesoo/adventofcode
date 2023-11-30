import re

def get_priority(letter):
    if re.match('[a-z]', letter):
        return ord(letter) - 96
    else:
        return ord(letter) - 38
    
with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

p_sum = 0
for i in inlines:
    half_len = int(len(i)/2)
    first = i[:half_len]
    second = i[half_len:]
    for item in first:
        if item in second:
            p_sum += get_priority(item)
            break

print (p_sum)

