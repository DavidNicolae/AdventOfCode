import re
import math

rules = {}
parts = []

def comparer(x, sg, y):
    if sg == '<':
        return x < y
    return x > y

def negate_condition(x, sg, y):
    if sg == '>':
        return (x, '<=', y)
    return (x, '>=', y)

def get_input():
    rule_flag = True
    with open('input.txt', 'r') as f:
        l = f.readline()
        while l:
            if not l.strip():
                rule_flag = False
                l = f.readline()
            if rule_flag:
                rule = l[:l.index('{')]
                rules[rule] = {}
                ops = l[l.index('{') + 1:-2].split(',')
                for op in ops:
                    if '<' in op:
                        sg = '<'
                    elif '>' in op:
                        sg = '>'
                    else:
                        rules[rule][None] = op
                        continue
                    op = re.split(r'<|>|:', op)
                    rules[rule][(op[0], sg, int(op[1]))] = op[2]
            else:
                parts.append({key: int(val) for key, val in zip(['x', 'm', 'a', 's'], re.findall(r'\d+', l))})
            l = f.readline()

def a():
    ans = 0
    for part in parts:
        rule = 'in'
        while rule:
            if rule == 'R':
                break
            if rule == 'A':
                ans += sum(part.values())
                break
            for op, next_rule in rules[rule].items():
                if op == None or len(op) == 3 and comparer(part[op[0]], op[1], op[2]):
                    rule = next_rule
                    break
    return ans
    
def b():
    accepted = []
    queue = [('in', [])]
    while queue:
        rule, conditions = queue.pop(0)
        if rule[-1] == 'A':
            accepted.append((rule, conditions))
            continue
        elif rule[-1] == 'R':
            continue
        for cond, r in rules[rule.split()[-1]].items():
            next_conditions = conditions[:]
            next_rule = rule + ' ' + r
            if cond != None:
                next_conditions.append(cond)
                conditions.append(negate_condition(*cond))
            queue.append((next_rule, next_conditions))
    
    ans = 0
    for _, conditions in accepted:
        d = {key: [1, 4000] for key in ['x', 'm', 'a', 's']}
        for type, op, val in conditions:
            if op == '>':
                d[type][0] = val + 1
            elif op == '>=':
                d[type][0] = val
            elif op == '<':
                d[type][1] = val - 1
            else:
                d[type][1] = val
        ans += math.prod(k[1] - k[0] + 1 for k in d.values())

    return ans

if __name__ == '__main__':
    get_input()
    print(a())
    print(b())