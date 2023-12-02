def get_input():
    f = open('input.txt', 'r')
    input = [line.strip() for line in f.readlines()]
    f.close()
    return input

def get_input2():
    with open('input.txt', 'r') as f:
        input = f.read()
    return input