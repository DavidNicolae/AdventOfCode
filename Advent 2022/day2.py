def get_input():
    f = open('input.txt', 'r')
    input = [line.strip().replace(' ', '') for line in f.readlines()]
    f.close()
    return input

d = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
d2 = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}

def ab():
    score_a = 0
    score_b = 0
    for line in get_input():
        score_a += d[line]
        score_b += d2[line]
    return score_a, score_b

print(ab())