from copy import copy

class Number:
    def __init__(self, val) -> None:
        self.val = val

def get_input():
    f = open('input.txt', 'r')
    numbers = []
    for line in f.readlines():
        numbers.append(Number(int(line)))
        if line == '0\n':
            zero_nr = numbers[-1]
    order = copy(numbers)
    f.close()
    return numbers, order, zero_nr

def a():
    sum = 0
    numbers, order, zero_nr = get_input()
    
    for nr in order:
        number = numbers[numbers.index(nr)]
        if number.val == 0:
            continue
        index = numbers.index(number)
        offset = abs(number.val) % (len(numbers) - 1)
        offset = -offset if number.val < 0 else offset
        pos = index + offset
        if pos >= len(numbers):
            pos = pos % len(numbers) + 1
        elif pos == 0:
            pos = 0 if offset >= 0 else len(numbers)
        popped = numbers.pop(index)
        numbers.insert(pos, popped)
        
    zero_index = numbers.index(zero_nr)
    for i in [1000, 2000, 3000]:
        index = zero_index + i % len(numbers)
        index = index % len(numbers)
        sum += numbers[index].val
    
    return sum

def b():
    key = 811589153
    sum = 0
    numbers, order, zero_nr = get_input()
    
    for number in numbers:
        number.val *= key
    
    for i in range(10):
        for nr in order:
            number = numbers[numbers.index(nr)]
            if number.val == 0:
                continue
            index = numbers.index(number)
            offset = abs(number.val) % (len(numbers) - 1)
            offset = -offset if number.val < 0 else offset
            pos = index + offset
            if pos >= len(numbers):
                pos = pos % len(numbers) + 1
            elif pos == 0:
                pos = 0 if offset >= 0 else len(numbers)
            popped = numbers.pop(index)
            numbers.insert(pos, popped)
        
    zero_index = numbers.index(zero_nr)
    for i in [1000, 2000, 3000]:
        index = zero_index + i % len(numbers)
        index = index % len(numbers)
        sum += numbers[index].val
        
    return sum

print(a())
print(b())