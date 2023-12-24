from collections import defaultdict

offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x, y):
    return x >= 0 and y >= 0 and x < len(map) and y < len(map[0])

def get_next(x, y, p1=True):
    if p1:
        if map[x][y] == '>':
            return [(x + offsets[0][0], y + offsets[0][1])]
        if map[x][y] == 'v':
            return [(x + offsets[1][0], y + offsets[1][1])]
        if map[x][y] == '<':
            return [(x + offsets[2][0], y + offsets[2][1])]
        if map[x][y] == '^':
            return [(x + offsets[3][0], y + offsets[3][1])]
    next_pos = []
    for x_inc, y_inc in offsets:
        next_x, next_y = x + x_inc, y + y_inc
        if is_valid(next_x, next_y) and map[next_x][next_y] != '#':
            next_pos.append((next_x, next_y))
    return next_pos

def a(queue, adj, p1=True):
    while queue:
        cost, (x, y), prev, visited = queue.pop()
        if (x, y) == end:
            adj[prev].append((end, cost))
            continue
        next_pos = [p for p in get_next(x, y, p1) if p not in visited]
        if len(next_pos) == 1:
            queue.append((cost + 1, next_pos[0], prev, visited | {next_pos[0]}))
        else:
            if ((x, y), cost) in adj[prev]:
                    continue
            adj[prev].append(((x, y), cost))
            if not p1:
                adj[(x, y)].append((prev, cost))
            for next_x, next_y in next_pos:
                queue.append((1, (next_x, next_y), (x, y), {(x, y), (next_x, next_y)}))
    
    ans = 0
    queue = [(start, 0, {start})]
    while queue:
        cur, cost, visited = queue.pop()
        if cur == end:
            ans = max(ans, cost)
        for next, next_cost in adj[cur]:
            if next not in visited:
                queue.append((next, cost + next_cost, visited | {next}))

    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        map = f.read().split()
    start, end = (0, map[0].index('.')), (len(map) - 1, map[-1].index('.'))
    
    visited = {start}
    queue = [(0, start, start, visited)]
    print(a(queue, defaultdict(list)))
    
    visited = {start}
    queue = [(0, start, start, visited)]
    print(a(queue, defaultdict(list), p1=False))