import re
import numpy as np
from copy import copy, deepcopy

class Blueprint:
    
    def __init__(self, robots_cost, resources=np.array([0, 0, 0, 0]), robots=np.array([1, 0, 0, 0])) -> None:
        self.resources = resources
        self.robots = robots
        self.robots_cost = robots_cost

    def collect_resources(self):
        self.resources += self.robots 

    def get_next_states(self):
        next_states = [deepcopy(self)]
        left_resources = self.resources - self.robots_cost
        for index, resources in enumerate(left_resources):
            if np.any(resources < 0):
                continue
            new_robots = copy(self.robots)
            new_state = Blueprint(self.robots_cost, resources=resources, robots=new_robots)
            new_state.collect_resources()
            new_state.robots[index] += 1
            next_states.append(new_state)
        next_states[0].collect_resources()
        return next_states

def get_input():
    blueprints = []
    f = open('input.txt', 'r')
    for line in f.readlines():
        line = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
        robots_cost = np.array([[line[1], 0, 0, 0],
                                [line[2], 0, 0, 0],
                                [line[3], line[4], 0, 0],
                                [line[5], 0, line[6], 0]])
        blueprints.append(Blueprint(robots_cost))
    return blueprints

def state_key(state):
    return tuple(np.flip(state.resources + state.robots))

def ab():
    quality1, quality2 = 0, 1
    time1, time2 = 24, 32
    blueprints = get_input()
    for index, blueprint in enumerate(blueprints):
        queue = [(blueprint)]
        for _ in range(time1):
            next_queue = []
            while queue:
                state = queue.pop(0)
                next_queue.extend(state.get_next_states())
            next_queue = sorted(next_queue, key=lambda l: tuple(np.flip(l.resources + l.robots)))
            queue = next_queue[-2000:]
        queue = sorted(queue, key=lambda l: l.resources[3])
        quality1 += (index + 1) * queue[-1].resources[3]
        
    for index, blueprint in enumerate(blueprints[0:3]):
        queue = [(blueprint)]
        for _ in range(time2):
            next_queue = []
            while queue:
                state = queue.pop(0)
                next_queue.extend(state.get_next_states())
            next_queue = sorted(next_queue, key=lambda l: tuple(np.flip(l.resources + l.robots)))
            queue = next_queue[-2000:]
        queue = sorted(queue, key=lambda l: l.resources[3])
        quality2 *= queue[-1].resources[3]
    return quality1, quality2

print(ab())