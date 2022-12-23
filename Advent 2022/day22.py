def get_input():
    map = {}
    f = open('input.txt', 'r')
    index = 0
    while True:
        line = f.readline()
        if line == '\n':
            break
        line = line[:-1]
        map[index]= {}
        for idx, pos in enumerate(line):
            if pos == ' ':
                continue
            map[index][idx]= pos
        index += 1

    moves = f.readline()
    start = (0, list(map[0].keys())[0])
    return map, moves, start

def rotate90(direction, rotation):
    if rotation == 'R':
        direction += 1
    else:
        direction -= 1
    if direction == 4:
        direction = 0
    elif direction == -1:
        direction = 3
    return direction

def a():
    offsets = {0: 1, 1: 1, 2: -1, 3: -1}
    direction = 0
    map, moves, start = get_input()
    moves = moves.replace('R', ' R ').replace('L', ' L ').split(' ')
    
    for move in moves:
        if move == 'R' or move == 'L':
            direction = rotate90(direction, move)
        else:
            x = start[0]
            y = start[1]
            if direction == 0 or direction == 2:
                for _ in range(int(move)):
                    y += offsets[direction]
                    if y not in map[x]:
                        if direction == 0:
                            y = list(map[x].keys())[0]
                        else:
                            y = list(map[x].keys())[-1]
                    if map[x][y] == '#':
                        break
                    start = (x, y)
            else:
                for _ in range(int(move)):
                    x += offsets[direction]
                    if x not in map or y not in map[x]:
                        if direction == 1:
                            x = 0
                            while y not in map[x]:
                                x += 1
                        else:
                            x = len(map) - 1
                            while y not in map[x]:
                                x -= 1
                    if map[x][y] == '#':
                        break
                    start = (x, y)
    return 1000 * (start[0] + 1) + 4 * (start[1] + 1) + direction

def b():
    offsets = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    direction = 0
    map, moves, start = get_input()
    moves = moves.replace('R', ' R ').replace('L', ' L ').split(' ')
    ok = set()
    
    for move in moves:
        if move == 'R' or move == 'L':
            direction = rotate90(direction, move)
        else:
            x = start[0]
            y = start[1]
            for _ in range(int(move)):
                x += offsets[direction][0]
                y += offsets[direction][1]
                new_direction = direction
                if x > 99 and x < 150 and y > 99 and direction == 0:
                    x = 149 - x
                    y = 149
                    new_direction = 2
                    ok.add(0)
                elif x > 99 and x < 150 and y < 0 and direction == 2:
                    x = 149 - x
                    y = 50
                    new_direction = 0
                    ok.add(1)
                elif x < 100 and y < 50 and direction == 3:
                    x = y + 50
                    y = 50
                    new_direction = 0
                    ok.add(2)
                elif x > 199 and direction == 1:
                    x = 0
                    y = y + 100
                    new_direction = 1
                    ok.add(3)
                elif x > 149 and y > 49 and direction == 1:
                    x = y + 100
                    y = 49
                    new_direction = 2
                    ok.add(4)
                elif x > 149 and y < 0 and direction == 2:
                    y = x - 100
                    x = 0
                    new_direction = 1
                    ok.add(5)
                elif x > 149 and x < 200 and y > 49 and direction == 0:
                    y = x - 100
                    x = 149
                    new_direction = 3
                    ok.add(6)
                elif x > 49 and x < 100 and y < 50 and direction == 2:
                    y = x - 50
                    x = 100
                    new_direction = 1
                    ok.add(7)
                elif x > 49 and x < 100 and y > 99 and direction == 0:
                    y = x + 50
                    x = 49
                    new_direction = 3
                    ok.add(8)
                elif x > -1 and x < 50 and y < 50 and direction == 2:
                    x = 149 - x
                    y = 0
                    new_direction = 0
                    ok.add(9)
                elif x < 0 and y < 100 and direction == 3:
                    x = 100 + y
                    y = 0
                    new_direction = 0
                    ok.add(10)
                elif x < 0 and y > 99 and direction == 3:
                    x = 199
                    y = y - 100
                    new_direction = 3
                    ok.add(11)
                elif x > -1 and x < 50 and y > 149 and direction == 0:
                    x = 149 - x
                    y = 99
                    new_direction = 2
                    ok.add(12)
                elif x > 49 and y > 99 and y < 150 and direction == 1:
                    x = y - 50
                    y = 99
                    new_direction = 2
                    ok.add(13)
                if map[x][y] == '#':
                    break
                direction = new_direction
                start = (x, y)
    return 1000 * (start[0] + 1) + 4 * (start[1] + 1) + direction

print(a())
print(b())
