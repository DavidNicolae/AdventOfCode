import re

class Broadcast:
    def __init__(self, name) -> None:
        self.name = name
        self.dest = []
        
    def process_signal(self, signal, sender=None):
        return self, signal

class Flip_Flop:
    def __init__(self, name) -> None:
        self.name = name
        self.dest = []
        self.off = True
        
    def process_signal(self, signal, sender=None):
        if signal == 1 or not self.dest:
            return None, None
        if self.off:
            signal = 1
        self.off = not self.off
        return self, signal

class Conjunction:
    def __init__(self, name) -> None:
        self.name = name
        self.dest = []
        self.memory = {}
        
    def process_signal(self, signal, sender=None):
        self.memory[sender] = signal
        if all(sg == 1 for sg in self.memory.values()):
            signal = 0
        else:
            signal = 1
        return self, signal

def a_b():
    signals = [0, 0]
    ans = []
    i = 1
    while i and len(ans) < 4:
        if i <= 1000:
            signals[0] += 1
        queue = [(broadcast, 0)]
        while queue:
            module, signal = queue.pop(0)
            for destination in module.dest:
                next_module, next_signal = destination.process_signal(signal, module)
                if destination.name in loop and signal == 1 and next_signal == 0:
                    ans.append(i)
                if i <= 1000:
                    signals[signal] += 1
                if next_module:
                    queue.append((next_module, next_signal))
        i += 1
    product = 1
    for e in ans:
        product *= e
    return signals[0] * signals[1], product

if __name__ == '__main__':
    modules = {}
    rev_modules = {}
    dest = []
    with open('input.txt', 'r') as f:
        l = f.readline()
        while l:
            l = re.split(r'\s*->\s*|,\s*', l.strip())
            name = l[0][1:]
            if l[0][0] == '%':
                new = Flip_Flop(name)
            elif l[0][0] == '&':
                new = Conjunction(l[0][1:])
            else:
                name = l[0]
                new = Broadcast(name)
                broadcast = new
            modules[name] = new
            dest.append(l[1:])
            l = f.readline()
    
    for i, d in enumerate(modules):
        for name in dest[i]:
            if name not in modules:
                new = Flip_Flop(name)
                modules[d].dest.append(new)
                if new.name in rev_modules:
                    rev_modules[new.name].append(modules[d])
                else:
                    rev_modules[new.name] = [modules[d]]
                continue
            modules[d].dest.append(modules[name])
            if name in rev_modules:
                rev_modules[name].append(modules[d])
            else:
                rev_modules[name] = [modules[d]]
            if isinstance(modules[name], Conjunction):
                modules[name].memory[modules[d]] = 0
    
    queue = [rev_modules['rx'][0]]
    visited = {rev_modules['rx'][0]}
    repr = set()
    while queue:
        module = queue.pop()
        for m in rev_modules[module.name]:
            if m.name == 'broadcaster' or m.name in visited:
                repr.add(module)
                continue
            else:
                queue.append(m)
                visited.add(m.name)
    
    loop = set()
    for module in repr:
        while not isinstance(module, Conjunction):
            for m in rev_modules[module.name]:
                module = m
                break
        loop.add(module.name)

    print(a_b())