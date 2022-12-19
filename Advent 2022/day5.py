PART = 'b'

def ab():
    f = open('input.txt', 'r')
    input = []
    stacks = {}
    for line in f.readlines():
        line = line.strip('\n')
        if '[' in line:
            input.append(line)
        elif line.startswith(' 1'):
            for index, c in enumerate(line):
                if c != ' ':
                    stacks[int(c)] = []
                    for ln in input:
                        if ln[index] == ' ':
                            continue
                        stacks[int(c)].insert(0, (ln[index]))
        elif line.startswith('move'):
            line = line.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ')
            nr, frm, to = map(lambda x: int(x), line.split(' '))
            
            if PART == 'a':
                for _ in range(nr):
                    stacks[to].append(stacks[frm].pop())
            else:
                stacks[to].extend(stacks[frm][-nr:])
                stacks[frm] = stacks[frm][:-nr]
    f.close()
    i = 1
    result = ''
    while i in stacks:
        result += stacks[i].pop()
        i += 1
    return result

print(ab())

