def get_input():
    monkeys = {}
    f = open('input.txt', 'r')
    
    for line in f.readlines():
        line = line.strip().split(' ')
        if len(line) > 2:
            monkeys[line[0][:-1]] = (line[1:])
        else:
            monkeys[line[0][:-1]] = int(line[1])
    return monkeys
    
def calculate(monkeys, left_op, right_op, path):
    total = left_op if left_op != '?' else right_op
    for index, monkey in enumerate(path[:-1]):
        tmp = monkeys[monkey]
        known_index = 0 if type(tmp[0]) == type(int()) else 2
        known_monkey = tmp[known_index]
        if tmp[1] == '+':
            total -= known_monkey
        elif tmp[1] == '-':
            if known_index == 0:
                total = known_monkey - total
            else:
                total += known_monkey
        elif tmp[1] == '*':
            total = total // known_monkey
        else:
            if known_index == 0:
                total = known_monkey // total
            else:
                total *= known_monkey
    return total

def yell(monkeys, root, path):
    val = monkeys[root]
    if type(val) == type(int()):
        return val
    if val == '?':
        path.insert(0, root)
        return val
    
    left_op = yell(monkeys, val[0], path)
    right_op = yell(monkeys, val[2], path)
    
    if val[1] == '=':
        return calculate(monkeys, left_op, right_op, path)
    
    if left_op != '?' and right_op != '?':
        if val[1] == '+':
            return left_op + right_op
        elif val[1] == '-':
            return left_op - right_op
        elif val[1] == '/':
            return left_op // right_op
        elif val[1] == '*':
            return left_op * right_op
    else:
        path.insert(0, root)
        if left_op == '?':
            monkeys[root][2] = right_op
        else:
            monkeys[root][0] = left_op
        return '?'
        
def a():
    root = 'root'
    monkeys = get_input()
    return yell(monkeys, root, [])

def b():
    root = 'root'
    me = 'humn'
    monkeys = get_input()
    monkeys[root][1] = '='
    monkeys[me] = '?'
    path = []
    res = yell(monkeys, root, path)
    return res

print(a())
print(b())
