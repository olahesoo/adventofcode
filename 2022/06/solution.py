with open('input') as infile:
    inlines = [i.strip() for i in infile]

def all_different(buffer):
    return len(buffer) == len(set(buffer))

def start_index(word, count):
    index = count
    buffer = list(word[:count])
    while not all_different(buffer):
        index += 1
        buffer.pop(0)
        buffer.append(word[index-1])
    return index

print (start_index(inlines[0], 4))

