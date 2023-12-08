from math import lcm

def a():
    d = {}
    steps = 0
    with open('input.txt', 'r') as f:
        moves = f.readline().strip()
        f.readline()
        line = f.readline()
        while line:
            line = line.strip()
            d[line[0:3]] = (line[7:10], line[12:15])
            line = f.readline()

    i = 0
    pos = 'AAA'
    end = 'ZZZ'
    while pos != end:
        if moves[i] == 'L':
            pos = d[pos][0]
        else:
            pos = d[pos][1]
        steps += 1
        i += 1
        if i == len(moves):
            i  = 0
    
    return steps

def b():
    d = {}
    pos = []
    with open('input.txt', 'r') as f:
        moves = f.readline().strip()
        f.readline()
        line = f.readline()
        while line:
            line = line.strip()
            start, left, right = line[0:3], line[7:10], line[12:15]
            d[start] = (left, right)
            if start.endswith('A'):
                pos.append(start)
            line = f.readline()

    periods = []
    for j in range(len(pos)):
        i = 0
        steps = 0
        start = pos[j]
        while not start.endswith('Z'):
            if moves[i] == 'L':
                start = d[start][0]
            else:
                start = d[start][1]
            steps += 1
            i += 1
            if i == len(moves):
                i = 0
        periods.append(steps)
    
    return lcm(*periods)
        
if __name__ == '__main__':
    print(a())
    print(b())