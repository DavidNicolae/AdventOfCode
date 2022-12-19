def get_input():
    f = open('input.txt', 'r')
    input = [line.strip() for line in f.readlines()]
    f.close()
    return input

def a():
    nr = 0
    lines = get_input()
    for line in lines:
        pair = line.split(',')
        x1, y1 = pair[0].split('-')
        x2, y2 = pair[1].split('-')
        if int(x1) <= int(x2) and int(y1) >= int(y2) or int(x1) >= int(x2) and int(y1) <= int(y2):
            nr += 1
    return nr

def b():
    nr = 0
    lines = get_input()
    for line in lines:
        pair = line.split(',')
        x1, y1 = pair[0].split('-')
        x2, y2 = pair[1].split('-')
        # print(x1, y1, x2, y2)
        if int(x2) >= int(x1) and int(x2) <= int(y1) or int(y2) >= int(x1) and int(y2) <= int(y1):
            nr += 1
        elif int(x1) >= int(x2) and int(x1) <= int(y2) or int(y1) >= int(x2) and int(y1) <= int(y2):
            nr += 1
        else:
            print(x1, y1, x2, y2)
    return nr

print(a())
print(b())