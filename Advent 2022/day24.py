neighbours_offsets = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]

def get_input():
    map = {}
    borders = set()
    f = open('input.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                borders.add((i, j))
            elif c == '>' or c == '^' or c == '<' or c == 'v':
                map[(i, j)] = c
    return map, borders, len(lines) - 2, len(lines[0]) - 2 

def cycle(map, offsets):
    new_map = {}
    for pos, val in map.items():
        for v in val:
            offset = offsets[v]
            new_pos = [pos[0] + offset[0], pos[1] + offset[1]]
            if new_pos[0] > pos[0]:
                if new_pos[0] > offset[2]:
                    new_pos[0] = offset[3]
            elif new_pos[0] < pos[0]:
                if new_pos[0] < offset[2]:
                    new_pos[0] = offset[3]
            elif new_pos[1] > pos[1]:
                if new_pos[1] > offset[2]:
                    new_pos[1] = offset[3]
            elif new_pos[1] < pos[1]:
                if new_pos[1] < offset[2]:
                    new_pos[1] = offset[3]
            new_pos = tuple(new_pos)
            if new_pos not in new_map: 
                new_map[new_pos] = v
            else:
                new_map[new_pos] += v
    return new_map
        
def get_neighbours(start, map, borders):
    neighbours = [(start[0] + offset[0], start[1] + offset[1]) for offset in neighbours_offsets]
    neighbours = [n for n in neighbours if n not in borders and n not in map]
    return neighbours

def BFS(start, end, map, borders, offsets):
    moves = 0
    queue = [(start.pop(0))]
    while True:
        map = cycle(map, offsets)
        moves += 1
        next_queue = set()
        while queue:
            pos = queue.pop(0)
            if pos == end[0]:
                end.pop(0)
                if start:
                    next_queue = {start.pop(0)}
                    break
                else:
                    return moves - 1
            next_queue.update(get_neighbours(pos, map, borders))
        queue = list(next_queue)

def ab():
    map, borders, max_x, max_y = get_input()
    offsets = {'v': (1, 0, max_x, 1), '^': (-1, 0, 1, max_x),
               '>': (0, 1, max_y, 1), '<': (0, -1, 1, max_y)}
    start = (0, 1)
    end = (max_x + 1, max_y)
    borders.add((-1, 1))
    borders.add((max_x + 2, max_y))
    
    res1 = BFS([start], [end], map, borders, offsets)
    res2 = BFS([start, end, start], [end, start, end], map, borders, offsets)
    
    return res1, res2 
    
print(ab())