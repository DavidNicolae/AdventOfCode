import math

PART = 'b'
if PART == 'a':
    ROUNDS = 20
else:
    ROUNDS = 10000
CONST_A = 3
CONST_B = 1

class Monkey:
    def __init__(self, items, op, token, cond, monkey1, monkey2) -> None:
        self.count = 0
        self.items = items
        self.op = op
        self.token = token
        self.cond = cond
        self.monkey1 = monkey1
        self.monkey2 = monkey2
        
    def do_op_a(self):
        if self.op == '+':
            self.items = [(item + self.get_token(item)) // CONST_A for item in self.items]
        if self.op == '*':
            self.items = [item * self.get_token(item) // CONST_A for item in self.items]
            
    def do_op_b(self):
        if self.op == '+':
            self.items = [(item + self.get_token(item)) % CONST_B for item in self.items]
        if self.op == '*':
            self.items = [(item * self.get_token(item)) % CONST_B for item in self.items]
    
    def get_token(self, item):
        if self.token == 'old':
            return item
        return self.token

def get_input() -> list():
    monkeys = []
    f = open('input.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        if line.startswith('Starting'):
            items = [int(item) for item in line.split(': ')[1].split(', ')]
        elif line.startswith('Operation'):
            line = line.split('=')[1].split(' ')
            op = line[2]
            token = line[3]
            if token != 'old':
                token = int(token)
        elif line.startswith('Test'):
            cond = int(line.split('by ')[1])
            global CONST_B
            CONST_B *= cond
        elif line.startswith('If true'):
            monkey1 = int(line.split('monkey ')[1])
        elif line.startswith('If false'):
            monkey2 = int(line.split('monkey ')[1])
        elif line == '':
            monkeys.append(Monkey(items, op, token, cond, monkey1, monkey2))
    monkeys.append(Monkey(items, op, token, cond, monkey1, monkey2))
    f.close()
    return monkeys

def ab():
    monkeys = get_input()
    for _ in range(ROUNDS):
        for monkey in monkeys:
            monkey.count += len(monkey.items)
            if PART == 'a':
                monkey.do_op_a()
            else:
                monkey.do_op_b()
            for item in monkey.items:
                if item % (monkey.cond) == 0:
                    monkeys[monkey.monkey1].items.append(item)
                else:
                    monkeys[monkey.monkey2].items.append(item)
            monkey.items = []
    monkeys.sort(key= lambda m: m.count, reverse=True)
    return monkeys[0].count * monkeys[1].count

print(ab())