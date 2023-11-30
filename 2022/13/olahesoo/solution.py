def compare(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return True
        elif second < first:
            return False
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
            return True
        elif len(second) <= index:
            return False
        else:
            comparison = compare(first[index], second[index])
            index += 1
    return comparison

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

pairs = []
index = 0
while index < len(inlines):
    pairs.append((eval(inlines[index]), eval(inlines[index + 1])))
    index += 3

output = 0
for (i, pair) in enumerate(pairs):
    if compare(*pair):
        output += i + 1

print(output)

