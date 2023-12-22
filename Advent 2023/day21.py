inc = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def is_valid(x, y):
    return garden[x % max_x][y % max_y] != '#'

def a(x, y, max_steps):
    ans = 0
    queue = [(x, y, 0)]
    visited = {(x, y)}
    while queue:
        x, y, steps = queue.pop(0)
        if steps % 2 == max_steps % 2:
            ans += 1
        if steps <= max_steps:
            for next_x, next_y in [(x + inc_x, y + inc_y) for inc_x, inc_y in inc]:
                if is_valid(next_x, next_y) and (next_x, next_y) not in visited:
                    queue.append((next_x, next_y, steps + 1))
                    visited.add((next_x, next_y))
    return ans

if __name__ == '__main__':
    garden = []
    max_steps = 26501365
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            garden.append(line.strip())
            if 'S' in line:
                x, y = len(garden) - 1, line.index('S')
            line = f.readline()
    max_x = len(garden)
    max_y = len(garden[0])
    print(a(x, y, 64))
    f0 = a(x, y, x)
    f1 = a(x, y, x + max_x)
    f2 = a(x, y, x + 2 * max_x)
    c_ = f0
    b_ = (4 * f1 - f2 - 3 * f0) // 2
    a_ = (f2 - 2 * f1 + f0) // 2
    f = lambda x: x ** 2 * a_ + x * b_ + c_
    x = (max_steps - x) // max_x
    print(f(x))