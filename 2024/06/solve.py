import copy
import subprocess
from time import time as time


import timeit

class Guard():
    def __init__(self, x, y, direction):
        # x, y coordinates
        # direction:
        # up: (0, -1)
        # right: (1, 0)
        # down: (0, 1)  
        # left: (-1, 0)
        self.x                      = x
        self.y                      = y
        self.original_x             = x
        self.original_y             = y
        self.direction              = direction
        self.original_direction     = direction
        self.debug                  = True
        self.visited                = set()
        self.visited_with_direction = set()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.direction = self.original_direction
        self.visited = set()
        self.visited_with_direction = set()

    def set_game_map(self, game_map):
        self.game_map = copy.deepcopy(game_map)

    def add_obstacle(self, x, y):
        self.game_map[y][x] = '#'

    def in_a_loop(self):
        return (self.x, self.y, self.direction) in self.visited_with_direction

    def get_places_visited(self):
        return len(self.visited) - 1

    def obstacle_in_front(self):
        return self.game_map[self.y + self.direction[1]][self.x + self.direction[0]] == '#'
    
    def end_of_map_in_front(self):
        return self.y + self.direction[1] < 0 or self.y + self.direction[1] >= len(self.game_map) or self.x + self.direction[0] < 0 or self.x + self.direction[0] >= len(self.game_map[0])

    def turn_right(self):
        if self.direction == (0, -1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, 1)
        elif self.direction == (0, 1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, -1)

    def take_step(self):
        self.visited.add((self.x, self.y))
        self.visited_with_direction.add((self.x, self.y, self.direction))
        self.x += self.direction[0]
        self.y += self.direction[1]
        if self.debug:
            self.game_map[self.y][self.x] = 'X'
            # subprocess.call('clear')
            # output = '\n'.join(' '.join(map(str, row)) for row in self.game_map)
            # print(output)

    def guard_step(self):
        if self.end_of_map_in_front():
            return False
        if self.obstacle_in_front():
            self.turn_right()
            return True
        else:
            self.take_step()
            return True

game_map = []
guard_position = []

with open('input', 'r') as f:
    for y, line in enumerate(f):
        game_map.append([])
        for x, char in enumerate(line.strip()):
            if char == '^':
                guard = Guard(x, y, (0, -1))
                char = 'X'
            game_map[y].append(char)

guard.set_game_map(game_map)

def part1():
    while guard.guard_step():
        pass

print(f'Part 1 execution time: {timeit.timeit(part1, number=1)}')
print(f'Part 1 solution: {guard.get_places_visited()}')


def part2():
    # for every position that the guard has visited:
    # - reset the guard to start position
    # - replace that position with an obstacle
    # - run simulation until either the guard falls of the map or is in a loop
    # - repeat
    loops = 0
    visited_in_part1 = copy.deepcopy(guard.visited)

    for x, y in visited_in_part1:
        if x == guard.original_x and y == guard.original_y:
            continue
        print(f'Adding obstacle to {x}, {y}')
        # reset guard
        guard.reset()
        guard.set_game_map(game_map.copy())
        # set obstacle
        guard.add_obstacle(x, y)
        # run simulation
        while True:
            if guard.in_a_loop():
                subprocess.call('clear')
                output = '\n'.join(' '.join(map(str, row)) for row in guard.game_map)
                print(output)
                print(f'Loop detected at {guard.x}, {guard.y}, {guard.direction}')
                loops += 1
                break
            if guard.guard_step():
                pass
            else:
                break
    return loops

start_time = time()
solution2 = part2()
print(f'Part 2 execution time: {time() - start_time}')
print(f'Part 2 solution: {solution2 + 1}')