"""
Given robots with an x,y position and an x,y speed. calculate their
location after x seconds, when the map wraps around
"""

debug    = False
fn       = 'input'
map_size = {
    'sample_12': (11,7),
    'input': (101,103)
}
map_x, map_y = map_size[fn]


robots = []
with open(fn, 'r') as f:
    for line in f:
        _p, _v = line.strip().split(' ')
        xpos, ypos = _p.split('=')[1].split(',')
        xvel, yvel = _v.split('=')[1].split(',')
        robots.append((int(xpos), int(ypos), int(xvel), int(yvel)))

def get_robot_positions(robots, seconds):
    positions = []
    for xpos, ypos, xvel, yvel in robots:
        positions.append((
            (xpos + seconds * xvel) % map_x,
            (ypos + seconds * yvel) % map_y,
        ))
    return positions

def print_map(positions):
    map = []
    for i in range(map_y):
        map.append([0] * map_x)

    for x, y in positions:
        map[y][x] += 1
    
    content = ''
    for line in map:
        for pos in line:
            if pos == 0: content += '.'
            else: content += str(pos)
        content += '\n'
    return content

def get_robots_per_quadrant(positions):
    quadrant_sums = [0, 0, 0, 0]
    dx, dy = (map_x) // 2, (map_y) // 2
    for x, y in positions:
        if x < dx and y < dy:
            quadrant_sums[0] += 1
        elif x < dx and y > dy:
            quadrant_sums[1] += 1
        elif x > dx and y < dy:
            quadrant_sums[2] += 1
        elif x > dx and y > dy:
            quadrant_sums[3] += 1

    return quadrant_sums

positions = get_robot_positions(robots, 100)
if debug: print(print_map(positions))

ans1 = 1
for q in get_robots_per_quadrant(positions):
    ans1 *= q
print(ans1)

for i in range(8, 10000, 101):
    print(f'Iteration: {i}')
    # print_map(get_robot_positions(robots, i))
    positions = get_robot_positions(robots, i)
    print(print_map(positions))

