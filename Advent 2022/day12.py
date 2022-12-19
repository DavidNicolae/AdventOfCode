from heapq import heappush, heappop

OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
STARTS = []

def get_start_positions(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'a':
                STARTS.append((i, j))

def get_input():
    f = open('input.txt', 'r')
    grid = []
    for index, line in enumerate(f.readlines()):
        if 'S' in line:
            start = (index, line.index('S'))
        if 'E' in line:
            end = (index, line.index('E'))
        grid.append(line.strip())
    return grid, start, end

def is_valid(grid, start, pos):
    x_0, y_0 = start
    x, y = pos
    
    if grid[x_0][y_0] == 'S':
        start = ord('a')
    else:
        start = ord(grid[x_0][y_0])
    
    if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
        return False
    
    if grid[x][y] == 'E':
        pos = ord('z')
    else:
        pos = ord(grid[x][y])
    if  pos - start > 1:
        return False
    
    return True

def get_neighbours(grid, pos):
    x, y = pos
    neighbours = [(x + offset[0], y + offset[1]) for offset in OFFSETS]
    neighbours = list(filter(lambda l: is_valid(grid, pos, l), neighbours))
    return neighbours

def h(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])
    
def astar(grid, start, end):
    steps = 0
    frontier = []
    heappush(frontier, (0 + h(start, end), start))
    g_cost = {start: (0, None)}
    
    while frontier:
        _, current = heappop(frontier)
        if current == end:
            break
         
        for neigh in get_neighbours(grid, current):
            neigh_cost = g_cost[current][0] + 1
            if neigh not in g_cost or neigh_cost < g_cost[neigh][0]:
                g_cost[neigh] = (neigh_cost, current)
                heappush(frontier, (neigh_cost + h(neigh, start), neigh))
    
    if current != end:
        return -1
    
    while end != None and end != start:
        steps += 1
        end = g_cost[end][1]
    
    return steps
    
def a():
    grid, start, end = get_input()
    result = astar(grid, start, end)
    return result

def b():
    grid, start, end = get_input()
    STARTS.append(start)
    get_start_positions(grid)
    result = astar(grid, STARTS[0], end)
    for start in STARTS[1:]:
        res = astar(grid, start, end)
        if res != -1 and res < result:
            result = res
    return result

# print(a())
print(b())
