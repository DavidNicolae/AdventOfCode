def a():
    ans = 0
    with open('input.txt', 'r') as f:
        input = f.read().split(',')
    for s in input:
        v = 0
        for c in s:
            v = (v + ord(c)) * 17 % 256
        ans += v
    
    return ans

def b():
    boxes = {i: [] for i in range(256)}
    lenses = {i: [] for i in range(256)}
    with open('input.txt', 'r') as f:
        input = f.read().split(',')
    for s in input:
        if s[-1] == '-':
            id = 0
            for c in s[:-1]:
                id = (id + ord(c)) * 17 % 256
            if s[:-1] in boxes[id]:
                index = boxes[id].index(s[:-1])
                boxes[id].pop(index)
                lenses[id].pop(index)
        else:
            id = 0
            for c in s[:-2]:
                id = (id + ord(c)) * 17 % 256
            focal = int(s[-1])
            if s[:-2] in boxes[id]:
                index = boxes[id].index(s[:-2])
                lenses[id][index] = focal
            else:
                boxes[id].append(s[:-2])
                lenses[id].append(focal)
    ans = 0
    for k, l in lenses.items():
        for idx, lense in enumerate(l):
            ans += (k + 1) * (idx + 1) * lense
    
    return ans

if __name__ == '__main__':
    print(a())
    print(b())