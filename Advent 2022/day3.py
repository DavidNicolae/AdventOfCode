def get_input():
    f = open('input.txt', 'r')
    input = f.readlines()
    f.close()
    return input

def a():
    score = 0
    for line in get_input():
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]
        occ = set()
        for c in left:
            if c in right and c not in occ:
                if ord(c) < 97:
                    score += ord(c) - 38
                else:
                    score += ord(c) - 96
                occ.add(c)
                break
    return score

def b():
    score = 0
    lines = get_input()
    for i in range(0, len(lines), 3):
        r1 = lines[i]
        r2 = lines[i + 1]
        r3 = lines[i + 2]
        for c in r1:
            if c in r2 and c in r3:
                if ord(c) < 97:
                    score += ord(c) - 38
                else:
                    score += ord(c) - 96
                break
    return score

print(a())
print(b())