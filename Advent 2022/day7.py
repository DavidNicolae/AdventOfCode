def get_input():
    f = open('input.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def print_rec(dir, tabs):
    s = ''
    for _ in range(tabs):
        s += '  '
    print(f'{s} {dir.name}, (dir)')
    for child in dir.children:
        if type(child) == Dir:
            print_rec(child, tabs + 1)
        else:
            print(f'{s}   {child}')

def calculate_size(dir, size_map):
    size = 0
    for child in dir.children:
        if type(child) == Dir:
            if child not in size_map:
                calculate_size(child, size_map)
            size += size_map[child]
        else:
            size += int(child[1])
    size_map[dir] = size
    return size_map

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []

def ab():
    lines = get_input()
    dir = Dir('/', None)
    for line in lines:
        command = line.split(' ')
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '/':
                    while dir.parent != None:
                        dir = dir.parent
                elif command[2] == '..':
                    dir = dir.parent
                else:
                    for child in dir.children:
                        if type(child) == Dir and child.name == command[2]:
                            dir = child
                            break
        elif command[0] == 'dir':
            dir.children.append(Dir(command[1], dir))
        else:
            dir.children.append((command[1], command[0]))

    while dir.parent != None:
        dir = dir.parent
    
    # print_rec(dir, 0)
    size_map = calculate_size(dir, {})
    used = size_map[dir]
    need_size = 30000000 - (70000000 - used) 
    total = 0
    need_total = 70000000
    for dir, size in size_map.items():
        if size <= 100000:
            total += size
        if size >= need_size and size < need_total:
            current = dir
            need_total = size
    return total, size_map[current]

print(ab())