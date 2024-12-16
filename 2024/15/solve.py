game_map     = []
instructions = []
with open('./sample_small_part2', 'r') as f:
    for y, line in enumerate(f):
        if any([char in line for char in ['@', '#', 'O', '.']]):
            game_map.append([])
            for x, char in enumerate(line.strip()):
                game_map[y].append(char)
                if char == '@':
                    robot_pos = (x, y)
        else:
            instructions += (list(line.strip()))

class Robot():
    def __init__(self, x, y, game_map, part2 = False):
        # x, y coordinates
        # direction:
        # up: (0, -1)
        # right: (1, 0)
        # down: (0, 1)  
        # left: (-1, 0)
        self.x                      = x
        self.y                      = y
        self.game_map = game_map if not part2 else self.embiggen(game_map)
        self.debug                  = True
        self.part2                  = part2

        self.direction_vectors = {
            '^': (0, -1),
            '>': (1, 0),
            'v': (0, 1),
            '<': (-1, 0)
        }

    def embiggen(self, game_map):
        """Embiggen the map. 
        # becomes ##
        O becomes []
        . becomes ..
        @ becomes @.

        Args:
            game_map (list(list)): y,x map
        """
        new_map = []
        for row in game_map:
            new_row = []
            for char in row:
                if char == '#':
                    new_row.append('#')
                    new_row.append('#')
                elif char == 'O':
                    new_row.append('[')
                    new_row.append(']')
                elif char == '.':
                    new_row.append('.')
                    new_row.append('.')
                elif char == '@':
                    new_row.append('@')
                    new_row.append('.')
            new_map.append(new_row)
        return new_map

    def move(self, direction):
        print(f'Move {direction}:')
        if not self.can_move(direction): return
        self.game_map[self.y][self.x] = '.'
        self.move_crates(direction)
        self.x += self.direction_vectors[direction][0]
        self.y += self.direction_vectors[direction][1]
        self.game_map[self.y][self.x] = '@'
    
    def can_move(self, direction):
        # check the row or column "in front" of the robot. Return True if there
        # is at least one empty space '.' before a wall '#'
        if not self.part2 or (self.part2 and (direction == '<' or direction == '>')):
            for i in range(1, len(self.game_map)):
                x = self.x + i * self.direction_vectors[direction][0]
                y = self.y + i * self.direction_vectors[direction][1]
                if self.game_map[y][x] == '#': return False
                if self.game_map[y][x] == '.': return True
        else:
            # same logic but if there is a crate in front, we need to check if 
            # there is an empty space between BOTH squares of the crate
            # example
            # @[]. -> can move
            # @
            # []
            # .. -> can move
            # @
            # []
            # .# -> can't move
            pass

    def move_crates(self, direction):
        """There may be crates 'O' in front. If there is, we move any number of
        them, so they fill the next free space. Multiple boxes may be moved
        together

        Args:
            direction (str): Direction string
        """
        crates_to_move = []
        for i in range(1, len(self.game_map)):
            x = self.x + i * self.direction_vectors[direction][0]
            y = self.y + i * self.direction_vectors[direction][1]
            if self.game_map[y][x] == 'O':
                # move the crate
                crates_to_move.append((x, y))
            if self.game_map[y][x] == '.': break
        for crate in crates_to_move[::-1]:
            x, y = crate
            self.game_map[y][x] = '.'
            self.game_map[y + self.direction_vectors[direction][1]][x + self.direction_vectors[direction][0]] = 'O'

    def print_map(self):
        content = ''
        for row in self.game_map:
            content += ''.join(row) + '\n'
        print(content)

def calculate_score(map):
    """For every crate "O", calculate 100 * y + x and sum it up

    Args:
        map (list(list)): y, x map
    """
    ans = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == 'O':
                ans += 100 * y + x
    return ans


robot = Robot(robot_pos[0], robot_pos[1], game_map, True)
for instruction in instructions:
    robot.move(instruction)
    robot.print_map()

print(calculate_score(robot.game_map))