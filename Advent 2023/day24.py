import re
import numpy as np
import sympy

def b():
    array = np.array(lines, float)
    p, v, t = (sympy.symbols(f'{ch}(:3)') for ch in 'pvt')
    equations = [
        array[i, j] + t[i] * array[i, 3 + j] - p[j] - v[j] * t[i] for i in range(3) for j in range(3)
    ]
    return sum(sympy.solve(equations, (*p, *v, *t))[0][:3])

def in_future(x, y, s1, s2):
    if s1[3] > 0 and x < s1[0]:
        return False
    if s1[3] < 0 and x > s1[0]:
        return False
    if s1[4] > 0 and y < s1[1]:
        return False
    if s1[4] < 0 and y > s1[1]:
        return False
    if s2[3] > 0 and x < s2[0]:
        return False
    if s2[3] < 0 and x > s2[0]:
        return False
    if s2[4] > 0 and y < s2[1]:
        return False
    if s2[4] < 0 and y > s2[1]:
        return False
    return True

def line_equation(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope, slope * x1, y1

def a(left, right):
    ans = 0
    for i, (_a, b, c) in enumerate(eq):
        for j, (d, e, f) in enumerate(eq[i + 1:], i + 1):
            r = (b + f - c - e) 
            t = (_a - d)
            if t == 0:
                continue
            x = r / t
            y = x * _a - b + c
            if left <= x <= right and left <= y <= right and in_future(x, y, lines[i], lines[j]):
                ans += 1

    return ans


if __name__ == '__main__':
    eq = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = [int(x) for x in re.split(r',\s*|\s@\s', lines[i])]
        eq.append(line_equation(lines[i][0], lines[i][1], lines[i][0] + lines[i][3], lines[i][1] + lines[i][4]))
    print(a(200000000000000, 400000000000000))
    print(b())