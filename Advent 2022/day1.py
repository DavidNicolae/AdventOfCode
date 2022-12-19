def get_input():
    f = open('input.txt', 'r')
    input = [line.strip() for line in f.readlines()]
    f.close()
    return input

def a():
    max_food = 0
    food = 0

    for line in get_input():
        if line != '':
            food += int(line)
        else:
            if food > max_food:
                max_food = food
            food = 0
    return(max_food)

def b():
    food = 0
    l = []

    for line in get_input():
        if line != '':
            food += int(line)
        else:
            l.append(food)  
            food = 0
    l.sort(key=lambda x: -x)
    return sum(l[:3])

print(a())
print(b())