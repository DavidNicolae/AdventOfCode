PART = 'b'

if PART == 'a':
    size = 3
else:
    size = 13

def get_input():
    f = open('input.txt', 'r')
    input = f.readline().strip()
    f.close()
    return input

def ab():
    line = get_input()
    for i in range(len(line) - size):
        signal = line[i:i + size + 1]
        occ = set()
        for c in signal:
            occ.add(c)
        if len(occ) == size + 1:
            return i + size + 1
    return -1

print(ab())