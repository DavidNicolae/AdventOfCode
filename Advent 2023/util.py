def get_input():
    f = open('input.txt', 'r')
    input = [line.strip() for line in f.readlines()]
    f.close()
    return input