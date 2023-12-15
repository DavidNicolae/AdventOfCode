def move_north(input):
    for i in range(len(input[0])):
        last_rock = -1
        for j in range(len(input)):
            if input[j][i] == 'O':
                last_rock += 1
                if last_rock != j :
                    input[last_rock][i] = 'O'
                    input[j][i] = '.'
            elif input[j][i] == '#':
                last_rock = j

def move_south(input):
    for i in range(len(input[0])):
        last_rock = len(input)
        for j in range(len(input) - 1, -1, -1):
            if input[j][i] == 'O':
                last_rock -= 1
                if last_rock != j :
                    input[last_rock][i] = 'O'
                    input[j][i] = '.'
            elif input[j][i] == '#':
                last_rock = j

def move_west(input):
    for i in range(len(input)):
        last_rock = -1
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                last_rock += 1
                if last_rock != j :
                    input[i][last_rock] = 'O'
                    input[i][j] = '.'
            elif input[i][j] == '#':
                last_rock = j

def move_east(input):
    for i in range(len(input)):
        last_rock = len(input)
        for j in range(len(input[0]) - 1, -1, -1):
            if input[i][j] == 'O':
                last_rock -= 1
                if last_rock != j :
                    input[i][last_rock] = 'O'
                    input[i][j] = '.'
            elif input[i][j] == '#':
                last_rock = j

def a():
    with open('input.txt', 'r') as f:
        input = [list(line.strip()) for line in f]
    height = len(input)
    move_north(input)
    load = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                load += height - i
    return load

def b():
    periods = {}
    const = 1000000000
    with open('input.txt', 'r') as f:
        input = [list(line.strip()) for line in f]
    state = ''.join([c for l in input for c in l])
    periods[state] = 0
    height = len(input)
    for cycle in range(1, const + 1):
        move_north(input)
        move_west(input)
        move_south(input)
        move_east(input)
        
        state = ''.join([c for l in input for c in l])
        if state in periods:
            left_range = (const - periods[state]) % (cycle - periods[state])
            break
        periods[state] = cycle
    
    for _ in range(left_range):
        move_north(input)
        move_west(input)
        move_south(input)
        move_east(input)
    
    load = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O':
                load += height - i

    return load

if __name__ == '__main__':
    print(a())
    print(b())