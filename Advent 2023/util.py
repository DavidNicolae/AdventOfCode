def get_input():
    with open('input.txt', 'r') as f:
        input = [line.strip() for line in f.readlines()]
    return input

def get_input2():
    with open('input.txt', 'r') as f:
        input = f.read()
    return input