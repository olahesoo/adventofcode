import re

def get_priority(letter):
    if re.match('[a-z]', letter):
        return ord(letter) - 96
    else:
        return ord(letter) - 38
    
with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

p_sum = 0
for i in range(0, len(inlines), 3):
    for item in inlines[i]:
        if item in inlines[i+1] and item in inlines[i+2]:
            p_sum += get_priority(item)
            break

print (p_sum)

