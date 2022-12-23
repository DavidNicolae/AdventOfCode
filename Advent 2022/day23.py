chosen_offsets = {'N': [(-1, -1), (-1, 0), (-1, 1)], 'S': [(1, -1), (1, 0), (1, 1)],
            'W': [(-1, -1), (0, -1), (1, -1)], 'E': [(-1, 1), (0, 1), (1, 1)]}
all_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

directions = ['N', 'S', 'W', 'E']

def get_input():
    elves = set()
    f = open('input.txt', 'r')
    for index, line in enumerate(f.readlines()):
        line = line.strip()
        for idx, e in enumerate(line):
            if e == '#':
                elves.add((index, idx))
    f.close()
    return elves

def cycle():
    directions.append(directions.pop(0))

def check_stopped(elf, elves):
    positions = [(elf[0] + pos[0], elf[1] + pos[1]) for pos in all_offsets]
    return True if elves.intersection(positions) == set() else False

def get_next_position(elf, elves):
    for direction in directions:
        offsets = chosen_offsets[direction]
        available = [(elf[0] + offset[0], elf[1] + offset[1]) for offset in offsets]
        if elves.intersection(available) == set():
            return available[1]
    return False

def a():
    elves = get_input()
    for _ in range(1, 11):
        stopped_elves = [check_stopped(elf, elves) for elf in elves]
        new_elves = set()
        temp = {}
        for index, elf in enumerate(elves):
            if stopped_elves[index] == True:
                new_elves.add(elf)
            else:
                pos = get_next_position(elf, elves)
                if pos == False:
                    new_elves.add(elf)
                else:
                    temp[index] = pos
        for key, val in temp.items():
            if list(temp.values()).count(val) > 1:
                new_elves.add(list(elves)[key])
            else:
                new_elves.add(val)
        
        elves = new_elves
        cycle()
    
    elves = list(elves)
    min_x, max_x = elves[0][0], elves[0][0]
    min_y, max_y = elves[0][1], elves[0][1]
    for elf in elves:
        if elf[0] < min_x:
            min_x = elf[0]
        elif elf[0] > max_x:
            max_x = elf[0]
        if elf[1] < min_y:
            min_y = elf[1]
        elif elf[1] > max_y:
            max_y = elf[1]
            
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)

def b():
    global directions 
    directions = ['N', 'S', 'W', 'E']
    elves = get_input()
    counter = 1
    while True:
        stopped_elves = [check_stopped(elf, elves) for elf in elves]
        new_elves = set()
        next_positions = {}
        for index, elf in enumerate(elves):
            if stopped_elves[index] == True:
                new_elves.add(elf)
            else:
                pos = get_next_position(elf, elves)
                if pos == False:
                    new_elves.add(elf)
                else:
                    next_positions[elf] = pos
        for index, elf in enumerate(elves):
            if elf in next_positions:
                if list(next_positions.values()).count(next_positions[elf]) == 1:
                    new_elves.add(next_positions[elf])
                else:
                    new_elves.add(elf)
        if new_elves == elves:
            break
        elves = new_elves
        cycle()
        counter += 1
        
    return counter

print(a())
print(b())