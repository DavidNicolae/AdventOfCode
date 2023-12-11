def p(const):
    ans = 0
    l, c = set(), set()
    pos = []

    with open('input.txt', 'r') as f:
        input = f.read().split('\n')

    for i in range(len(input[0])):
        if ''.join([s[i] for s in input]).find('#') == -1:
            c.add(i)
    for i, line in enumerate(input):
        if line.find('#') == -1:
            l.add(i)

    x = 0
    for x, line in enumerate(input):
        offset = 0
        while line:
            y = line.find('#', offset)
            if y != -1:
                pos.append((x, y))
                offset = y + 1
            else:
                break

    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            dist_x = sum(1 for e in range(min(pos[i][0], pos[j][0]), max(pos[i][0], pos[j][0])) if e in l) * const
            dist_y = sum(1 for e in range(min(pos[i][1], pos[j][1]), max(pos[i][1], pos[j][1])) if e in c) * const
            ans += abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) + dist_x + dist_y
    
    return ans
    
if __name__ == '__main__':
    print(p(const=2 - 1))
    print(p(const=1000000 - 1))