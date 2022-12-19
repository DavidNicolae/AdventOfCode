import sys
sys.setrecursionlimit(10**9)

class Tetris:

    def increment_move(self):
        self.move_index += 1
        if self.move_index == len(self.moves):
            self.move_index = 0
            
    def __init__(self, nr_rocks, rock_counter=0, rock_type=0) -> None:
        self.rock_type = rock_type
        self.nr_rocks = nr_rocks
        moves = self.get_input()
        self.moves = ''
        for index in range(len(moves)):
            self.moves += moves[index] + 'v'
        self.blocked = {(0, i) for i in range(7)}
        self.move_index = -1
        self.rock_counter = rock_counter
        self.rock = Rock(self.rock_type, 4)
    
    def change_rock_type(self):
        self.rock_type += 1
        if self.rock_type == 5:
            self.rock_type = 0
    
    def get_input(self):
        f = open('input.txt', 'r')
        line = f.readline().strip()
        f.close()
        return line
    
    def generate_game(self):
        max_x = 0
        tracked = {}
        while self.rock_counter < self.nr_rocks:
            while True:                
                self.increment_move()
                key = (self.rock_type, self.move_index)
                if key in tracked:
                    prev_rock_counter, height = tracked[key]
                    interval = self.rock_counter - prev_rock_counter
                    if self.rock_counter % interval == self.nr_rocks % interval:
                        cycle_height = max_x - height
                        rocks_in_cycle = self.nr_rocks - prev_rock_counter
                        cycles = (rocks_in_cycle // interval)
                        return height + (cycle_height * cycles)
                else:
                    tracked[key] = (self.rock_counter, max_x)
                if self.rock.move_rock(self.moves[self.move_index], self.blocked) == False:
                    break
            max_x = max(max_x, max([pos[0] for pos in self.rock.positions]))
            self.blocked.update(self.rock.positions)
            self.rock_counter += 1
            self.change_rock_type()
            self.rock = Rock(self.rock_counter % 5, max_x + 4)
        return max_x
        
        
class Rock:
    OFFSETS = {'>': (0, 1), '<': (0, -1), 'v':(-1, 0)}
    
    def __init__(self, type, start) -> None:
        if type == 0:
            self.positions = [(start, 2 + offset) for offset in range(4)]
        elif type == 1:
            self.positions = [(start + 1, 2), (start + 1, 3), (start + 1, 4), (start, 3), (start + 2, 3)]
        elif type == 2:
            self.positions = [(start, 2), (start, 3), (start, 4), (start + 1, 4), (start + 2, 4)]
        elif type == 3:
            self.positions = [(start + offset, 2) for offset in range(4)]
        else:
            self.positions = [(start, 2), (start, 3), (start + 1, 2), (start + 1, 3)]
            
    def move_rock(self, move, blocked):
        offset = Rock.OFFSETS[move]
        new_positions = [(pos[0] + offset[0], pos[1] + offset[1]) for pos in self.positions]
        if move == 'v':
            for pos in new_positions:
                if pos in blocked:
                    return False
            self.positions = new_positions
            return True
        else:
            ok = True
            for pos in new_positions:
                if pos[1] < 0 or pos[1] > 6 or pos in blocked:
                    ok = False
                    break
            if ok:
                self.positions = new_positions
            return True
    
def ab():
    answer1 = Tetris(2022).generate_game()
    answer2 = Tetris(1000000000000).generate_game()
    return answer1, answer2

print(ab())