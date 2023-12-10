N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}
down = {'|', '7', 'F'}

def a_b():
    with open('input.txt', 'r') as f:
        maze = f.read().split('\n')
    start = None
    for i in range(len(maze)):
        if start:
            break        
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                x, y = i, j
                break
    queue = []
    visited = {(x, y)}
    if N in d[maze[x + 1][y]]:
        queue.append(((x + 1, y), 1))
        visited.add((x + 1, y))
        down.add('S')
    if S in d[maze[x - 1][y]]:
        queue.append(((x - 1, y), 1))
        visited.add((x - 1, y))
    if E in d[maze[x][y - 1]]:
        queue.append(((x, y - 1), 1))
        visited.add((x, y - 1))
    if W in d[maze[x][y + 1]]:
        queue.append(((x, y + 1), 1))
        visited.add((x, y + 1))

    while queue:
        (x, y), cost = queue.pop(0)
        for offset in d[maze[x][y]]:
            next = (x + offset[0], y + offset[1])
            if next not in visited:
                queue.append((next, cost + 1))
                visited.add(next)
    
    counter = 0
    for i in range(len(maze)):
        up = False
        for j in range(len(maze[i])):
            if maze[i][j] in down and (i, j) in visited:
                up = not up
            if up and (i, j) not in visited:
                counter += 1
    
    return cost, counter

if __name__ == '__main__':
    print(a_b())