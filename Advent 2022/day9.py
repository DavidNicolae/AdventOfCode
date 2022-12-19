def get_input():
    f = open('input.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

DIRECTION = {'L': (0, -1), 'R':(0, 1), 'U': (-1, 0), 'D': (1, 0)}
DIAG = {'LU': (-1, -1), 'RU':(-1, 1), 'LD': (1, -1), 'RD': (1, 1)}

def a():
    visited = set()
    visited.add((0, 0))
    x_head, y_head, x_tail, y_tail = 0, 0, 0, 0
    for line in get_input():
        move, nr = line.split(' ')
        offset = DIRECTION[move]
        for _ in range(int(nr)):
            last_move = (x_head, y_head)
            x_head += offset[0]
            y_head += offset[1]
            if abs(x_head - x_tail) > 1 or abs(y_head - y_tail) > 1:
                visited.add(last_move)
                x_tail, y_tail = last_move
    return len(visited)

def b():
    visited = set()
    visited.add((0, 0))
    rope = [(0, 0) for _ in range(10)]
    for line in get_input():
        move, nr = line.split(' ')
        offset = DIRECTION[move]
        for _ in range(int(nr)):
            x_head, y_head = rope[9]
            rope[9] = (x_head + offset[0], y_head + offset[1])
            for index in range(len(rope) - 2, -1, -1):
                x_ahead, y_ahead = rope[index + 1]
                x_tail, y_tail = rope[index]
                if abs(x_ahead - x_tail) > 1 or abs (y_ahead - y_tail) > 1:
                    if x_ahead == x_tail:
                        if y_ahead > y_tail:
                            rope[index] = (x_tail, y_tail + 1)
                        else:
                            rope[index] = (x_tail, y_tail - 1)
                    elif y_ahead == y_tail:
                        if x_ahead > x_tail:
                            rope[index] = (x_tail + 1, y_tail)
                        else:
                            rope[index] = (x_tail - 1, y_tail)
                    else:
                        if x_ahead > x_tail and y_ahead > y_tail:
                            off = DIAG['RD']
                            rope[index] = (x_tail + off[0], y_tail + off[1])
                        elif x_ahead > x_tail and y_ahead < y_tail:
                            off = DIAG['LD']
                            rope[index] = (x_tail + off[0], y_tail + off[1])
                        elif x_ahead < x_tail and y_ahead > y_tail:
                            off = DIAG['RU']
                            rope[index] = (x_tail + off[0], y_tail + off[1])
                        elif x_ahead < x_tail and y_ahead < y_tail:
                            off = DIAG['LU']
                            rope[index] = (x_tail + off[0], y_tail + off[1])
            visited.add(rope[0])
    return len(visited)

print(a())
print(b())