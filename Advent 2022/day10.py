def get_input():
    f = open('input.txt', 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()
    return lines

def a():
    sum = 0
    cycle = 0
    x = 1
    input = get_input()
    for line in input:
        command = line.split(' ')
        if command[0] == 'noop':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                sum += cycle * x
        else:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                sum += cycle * x
            cycle += 1
            if (cycle - 20) % 40 == 0:
                sum += cycle * x
            x += int(command[1])
    print(cycle)
    return sum

def b():
    cycle = 0
    x = 1
    display = '.' * 40 * 6
    print(len(display))
    input = get_input()
    for command in input:
        cmd = command.split(' ')
        if cmd[0] == 'noop':
            cycle += 1
            for i in range(6):
                if x - 1 + i * 40 == cycle - 1 or x + i * 40 == cycle - 1 or x + 1 + i * 40 == cycle - 1:
                    display = display[:cycle - 1] + '#' + display[cycle:]
        else:
            cycle += 1
            for i in range(6):
                if x - 1 + i * 40 == cycle - 1 or x + i * 40 == cycle - 1 or x + 1 + i * 40 == cycle - 1:
                    display = display[:cycle - 1] + '#' + display[cycle:]
            cycle += 1
            for i in range(6):
                if x - 1 + i * 40 == cycle - 1 or x + i * 40 == cycle - 1 or x + 1 + i * 40 == cycle - 1:
                    display = display[:cycle - 1] + '#' + display[cycle:]
            x += int(cmd[1])
    return display

display = b()
print(len(display))
for i in range(0, len(display), 40):
    print(display[i:i + 40])