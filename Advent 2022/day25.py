COEF = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}

def get_input():
    f = open('input.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def convert(dec):
    output = ''
    rest = 0
    while dec != 0 or rest:
        remainder = dec % 5 + rest
        rest = 0
        if remainder > 2:
            rest = 1
        output = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[remainder] + output
        dec //= 5
    return output

def a():
    total = 0
    lines = get_input()
    for line in lines:
        for index, c in enumerate(line):
            total += 5 ** (len(line) - index - 1) * COEF[c]
    return convert(total)

print(a())