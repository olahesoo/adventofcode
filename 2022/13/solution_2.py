from functools import cmp_to_key

def compare(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return -1
        elif second < first:
            return 1
        else:
            return None
    if type(first) == int:
        first = [first]
    if type(second) == int:
        second = [second]
    comparison = None
    index = 0
    while comparison == None:
        if len(first) <= index and len(second) <= index:
            return None
        elif len(first) <= index:
            return -1
        elif len(second) <= index:
            return 1
        else:
            comparison = compare(first[index], second[index])
            index += 1
    return comparison

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

packets = []
for i in inlines:
    if i:
        packets.append(eval(i))

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(compare))

first_index = packets.index([[2]]) + 1
second_index = packets.index([[6]]) + 1

print(first_index * second_index)

