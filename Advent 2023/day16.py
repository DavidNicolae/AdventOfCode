split = {(0, '|'): (1, 3), (0, '-'): (0,), (0, '/'): (3,), (0, '\\'): (1,),
        (1, '|'): (1,), (1, '-'): (0, 2), (1, '/'): (2,), (1, '\\'): (0,),
        (2, '|'): (1, 3), (2, '-'): (2,), (2, '/'): (1,), (2, '\\'): (3,),
        (3, '|'): (3,), (3, '-'): (0, 2), (3, '/'): (0,), (3, '\\'): (2,)}

direction_x = {0: 0, 1: 1, 2: 0, 3: -1}
direction_y = {0: 1, 1: 0, 2: -1, 3: 0}

def a(beam, visited):
    max_x, max_y = len(grid), len(grid[0])
    
    def on_grid(x, y):
        if x >= 0 and y >= 0 and x < max_x and y < max_y:
            return True
        return False
    
    while beam:
        x, y, d = beam.pop(0)
        if grid[x][y] == '.':
            next_x, next_y = x + direction_x[d], y + direction_y[d]
            if on_grid(next_x, next_y) and (next_x, next_y, d) not in visited:
                beam.append((next_x, next_y, d))
                visited.add((next_x, next_y, d))
        else:
            for dr in split[(d, grid[x][y])]:
                next_x, next_y = x + direction_x[dr], y + direction_y[dr]
                if on_grid(next_x, next_y) and (next_x, next_y, dr) not in visited:
                    beam.append((next_x, next_y, dr))
                    visited.add((next_x, next_y, dr))
                
    
    return len(set((v[0], v[1]) for v in visited))

def b():
    energized = 0
    max_x, max_y = len(grid), len(grid[0])
    for i in range(max_y):
        energized = max(energized, a([(0, i, 1)], {(0, i, 1)}))
        energized = max(energized, a([(max_x - 1, i, 3)], {(max_x - 1, i, 3)}))
    for i in range(max_x):
        energized = max(energized, a([(i, 0, 0)], {(i, 0, 0)}))
        energized = max(energized, a([(i, max_y - 1, 2)], {(0, max_y - 1, 2)}))
    
    return energized
        
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        grid = f.read().split()
    print(a([(0, 0, 0)], {(0, 0, 0)}))
    print(b())
    