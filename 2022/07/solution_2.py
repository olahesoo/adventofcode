def get_dir_size(directory):
    dir_size = 0
    for i in directory.items():
        if type(i[1]) == int:
            dir_size += i[1]
        elif i[0] != '..':
            dir_size += get_dir_size(i[1])
    return dir_size

def get_all_dir_sizes(root):
    output = set()
    for i in root.items():
        if i[0] != '..' and type(i[1]) == dict:
            output.add((i[0], get_dir_size(i[1])))
            output = output.union(get_all_dir_sizes(i[1]))
    return output

with open('input') as infile:
    inlines = [i.strip() for i in infile.readlines()]

directories = {'/': {}}
current_pos = directories['/']
index = 1

while index < len(inlines):
    command = inlines[index]
    assert command[:2] == '$ '
    command = command[2:]
    if command == 'ls':
        index += 1
        while index < len(inlines) and inlines[index][0] != '$':
            item = inlines[index]
            if item[:3] == 'dir':
                if not current_pos.get(item[4:]):
                    current_pos[item[4:]] = {}
                    current_pos[item[4:]]['..'] = current_pos
            else:
                size, filename = item.split(' ')
                current_pos[filename] = int(size)
            index += 1
    else:
        assert command[:2] == 'cd'
        directory = command[3:]
        current_pos = current_pos[directory]
        index += 1

total_space = 70000000
required_space = 30000000
used_space = get_dir_size(directories['/'])
missing_space = required_space - (total_space - used_space)

dir_sizes = get_all_dir_sizes(directories)
to_delete = (None, total_space)
for i in dir_sizes:
    if i[1] >= missing_space and i[1] < to_delete[1]:
        to_delete = i

print(to_delete[1])

