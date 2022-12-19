def get_input():
    f = open('input.txt', 'r')
    lines = []
    for line in f.readlines():
        line = line.strip()
        line = line.replace(' -> ', ' ').replace(',', ' ').split(' ')
        line = [int(elem) for elem in line]
        lines.append(line)

    return lines

def is_valid(cave, x, y, max_x, max_y):
    if x < max_x and y > -1 and y < max_y:
        if cave[x][y] == 0:
            return 1
        else:
            return 2
    return -1

def a():
    counter = 0
    max_x = -1
    max_y = -1
    lines = get_input()
    for line in lines:
        tmp = max([elem for index, elem in enumerate(line) if index % 2 == 1])
        if tmp > max_x:
            max_x = tmp
        tmp = max([elem for index, elem in enumerate(line) if index % 2 == 0])
        if tmp > max_y:
            max_y = tmp
    max_x += 1
    max_y += 1
    cave = [[0 for _ in range(max_y)] for _ in range(max_x)]
    for line in lines:
        for i in range(0, len(line) - 2, 2):
            y0, x0 = line[i], line[i + 1]
            y1, x1 = line[i + 2], line[i + 3]
            if x0 == x1:
                for j in range(min(y0, y1), max(y0, y1) + 1):
                    cave[x0][j] = 1
            else:
                for j in range(min(x0, x1), max(x0, x1) + 1):
                    cave[j][y0] = 1
    while True:
        pos_x, pos_y = 0, 500
        ok = True
        while True:
            res = is_valid(cave, pos_x + 1, pos_y, max_x, max_y)
            if res == 1:
                pos_x += 1
                continue
            elif res == -1:
                ok = False
                break
            res = is_valid(cave, pos_x + 1, pos_y - 1, max_x, max_y)
            if res == 1:
                pos_x += 1
                pos_y -= 1
                continue
            elif res == -1:
                ok = False
                break
            res = is_valid(cave, pos_x + 1, pos_y + 1, max_x, max_y)
            if res == 1:
                pos_x += 1
                pos_y += 1
                continue
            elif res == -1:
                ok = False
                break
            break
        if ok:
            cave[pos_x][pos_y] = 1
            counter += 1
        else:
            break
    return counter

def is_valid2(cave, x, y, max_x):
    if x < max_x - 1:
        if not y in cave[x]:
            return 1
    return 2

def b():
    counter = 0
    max_x = -1
    lines = get_input()
    for line in lines:
        tmp = max([elem for index, elem in enumerate(line) if index % 2 == 1])
        if tmp > max_x:
            max_x = tmp
    max_x += 3
    cave = [set() for _ in range(max_x)]
    for line in lines:
        for i in range(0, len(line) - 2, 2):
            y0, x0 = line[i], line[i + 1]
            y1, x1 = line[i + 2], line[i + 3]
            if x0 == x1:
                for j in range(min(y0, y1), max(y0, y1) + 1):
                    cave[x0].add(j)
            else:
                for j in range(min(x0, x1), max(x0, x1) + 1):
                    cave[j].add(y0)
    while True:
        pos_x, pos_y = 0, 500
        ok = True
        while True:
            if 500 in cave[0]:
                ok = False
                break
            res = is_valid2(cave, pos_x + 1, pos_y, max_x)
            if res == 1:
                pos_x += 1
                continue
            res = is_valid2(cave, pos_x + 1, pos_y - 1, max_x)
            if res == 1:
                pos_x += 1
                pos_y -= 1
                continue
            res = is_valid2(cave, pos_x + 1, pos_y + 1, max_x)
            if res == 1:
                pos_x += 1
                pos_y += 1
                continue
            break
        if ok:
            cave[pos_x].add(pos_y)
            counter += 1
        else:
            break
    return counter

print(a())
print(b())