from util import get_input

offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def check_adj(x, y, m, n, lines):
    positions = [(x + off[0], y + off[1]) for off in offsets]
    positions = [(x, y) for (x, y) in positions if x >= 0 and x < m and y >= 0 and y < n]
    for (x, y) in positions:
        if lines[x][y].isdigit() == False and lines[x][y] != '.':
            return True
    return False

def a():
    ans = 0
    lines = get_input()
    m = len(lines)
    n = len(lines[0])
    for x, line in enumerate(lines):
        left, right = -1, -1
        for idx, c in enumerate(line):
            if c.isdigit():
                if left == -1:
                    left = idx
                right = idx
            if c.isdigit() == False or idx == len(line) - 1:
                if left != -1 and right != -1:
                    nr = int(line[left: right + 1])
                    for y in range(left, right + 1):
                        if check_adj(x, y, m, n, lines):
                            ans += nr
                            break
                    left, right = -1, -1

    return ans

dict = {}

def count_adj(x, left, right, m, n, lines, nr):
    positions = set([(x + off[0], y + off[1]) for off in offsets for y in range(left, right)])
    positions = [(x, y) for (x, y) in positions if x >= 0 and x < m and y >= 0 and y < n]
    for (x, y) in positions:
        if lines[x][y].isdigit() == False and lines[x][y] == '*':
            if (x, y) not in dict:
                dict[(x, y)] = [nr]
            else:
                dict[(x, y)].append(nr)

def b():
    ans = 0
    lines = get_input()
    m = len(lines)
    n = len(lines[0])
    for x, line in enumerate(lines):
        left, right = -1, -1
        for idx, c in enumerate(line):
            if c.isdigit():
                if left == -1:
                    left = idx
                right = idx
            if c.isdigit() == False or idx == len(line) - 1:
                if left != -1 and right != -1:
                    nr = int(line[left: right + 1])
                    count_adj(x, left, right + 1, m, n, lines, nr)
                    left, right = -1, -1
    for lst in dict.values():
        if len(lst) == 2:
            ans += lst[0] * lst[1]

    return ans

if __name__ == '__main__':
    print(a())
    print(b())
