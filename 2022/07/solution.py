def get_dir_size(directory):
    dir_size = 0
    for i in directory.items():
        if type(i[1]) == int:
            dir_size += i[1]
        elif i[0] != '..':
            dir_size += get_dir_size(i[1])
    return dir_size


def calculate_sum_of_subdirs(root, max_size):
    total_sum = 0
    for i in root.items():
        if type(i[1]) == dict and i[0] != '..':
            subdir_size = get_dir_size(i[1])
            if subdir_size <= max_size:
                total_sum += subdir_size
            total_sum += calculate_sum_of_subdirs(i[1], max_size)
    return total_sum


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

print(calculate_sum_of_subdirs(directories['/'], 100000))

