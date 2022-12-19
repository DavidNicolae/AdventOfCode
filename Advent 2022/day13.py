def get_input():
    PAIRS = []
    f = open('input.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        if line != '':
            PAIRS.append(line)
    return PAIRS

def get_elem(i, str):
    j = i + 1
    if str[i] == '[':
        count = 0
        while str[j] != ']' or count != 0:
            if str[j] == '[':
                count += 1
            elif str[j] == ']':
                count -= 1
            j += 1
        elem = str[i:j + 1]
    else:
        while j < len(str) and str[j] != ',':
            j += 1
        elem = str[i:j]
    return elem

def parse_input(str, lst):
    i = 0
    while i < len(str):
        elem = get_elem(i, str)
        if ']' not in elem:
            lst.append(int(elem))
        else:
            new_list = []
            parse_input(elem[1:-1], new_list)
            lst.append(new_list)
        i += len(elem) + 1

def evaluate(l1, l2):
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        e1 = l1[i]
        e2 = l2[j]
        if type(e1) == type(list()) and type(e2) == type(list()):
            is_ok = evaluate(e1, e2)
            if is_ok != 'eq':
                return is_ok
        elif type(e1) == type(int()) and type(e2) == type(int()):
            if e1 > e2:
                return False
            if e1 < e2:
                return True
        else:
            if type(e1) == type(int()):
                is_ok = evaluate([e1], e2)
            else:
                is_ok = evaluate(e1, [e2])
            if is_ok != 'eq':
                return is_ok
        i += 1
        j += 1
    if i < len(l1):
        return False
    if i == j and len(l1) == len(l2):
        return 'eq'
    return True


def parse_lists():
    lists = []
    pairs = get_input()
    for str in pairs:
        lst = []
        parse_input(str[1:-1], lst)
        lists.append(lst)
    return lists

def a():
    lists = parse_lists()
    result = 0
    for i in range(0, len(lists), 2):
        res = evaluate(lists[i], lists[i + 1])
        if res:
            result += i // 2 + 1
    return result

def b():
    result = 1
    div1 = [[2]]
    div2 = [[6]]
    lists = parse_lists()
    lists.append(div1)
    lists.append(div2)
    for i in range(0, len(lists)):
        for j in range(i + 1, len(lists)):
            if evaluate(lists[i], lists[j]) == False:
                temp = lists[i]
                lists[i] = lists[j]
                lists[j] = temp
    for i in range(len(lists)):
        if lists[i] == div1 or lists[i] == div2:
            result *= (i + 1)
    return result

print(a())
print(b())