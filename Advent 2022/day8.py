def get_input():
    f = open('input.txt', 'r')
    input = []
    for index, line in enumerate(f.readlines()):
        line = line.strip()
        input.append([])
        for c in line:
            input[index].append(int(c))
    return input

def a():
    input = get_input()
    counter = 0
    for k, line in enumerate(input):
        for i in range(len(line)):
            if k == 0 or k == len(input) - 1 or i == 0 or i == len(line) - 1:
                counter += 1
                continue
            left = max(max(line[:i]), -1)
            right = max(max(line[i + 1:]), -1)
            up = max(max([l[i] for l in input[:k]]), -1)
            down = max(max([l[i] for l in input[k + 1:]]), -1)
            if line[i] > left or line[i] > right or line[i] > up or line[i] > down:
                counter += 1
    return counter

def b():
    input = get_input()
    score = 0
    for k, line in enumerate(input):
        for i in range(len(line)):
            left = line[:i]
            right = line[i + 1:]
            up = [l[i] for l in input[:k]]
            down = [l[i] for l in input[k + 1:]]
            scr1, scr2, scr3, scr4 = 0, 0, 0, 0
            for j in range(len(left) - 1, -1, -1):
                scr1 += 1
                if left[j] >= line[i]:
                    break
            for tree in right:
                scr2 += 1
                if tree >= line[i]:
                    break
            for j in range(len(up) - 1, -1, -1):
                scr3 += 1
                if up[j] >= line[i]:
                    break
            for tree in down:
                scr4 += 1
                if tree >= line[i]:
                    break
            scr1 *= scr2 * scr3 * scr4
            if scr1 > score:
                score = scr1
    return score

print(a())
print(b())