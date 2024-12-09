from copy import deepcopy
from time import time as time

from collections import defaultdict

# input is a long int. alternatingly the numbers represent the length of a file
# and length of free space.
# we create two lists: one that represents if a block is free and taken, and a 
# second list with the file_ids of those blocks. ids start at 0 and increment

debug       = True
file_id     = 0
block_index = 0
files       = {}
free_spaces = defaultdict(list)
with open('./sample3', 'r') as f:
    chars = []
    for line in f:
        for char in line.strip():
            chars.append(int(char))

for idx, char in enumerate(chars):
    # this means it is a file
    if not idx%2:
        files[file_id] = [block_index, char]
        file_id += 1
    else:
        free_spaces[char].append(block_index)
    block_index += char

# for some reason this does not work. it works on most examples but not on the
# real input. it's pretty fast though
def defrag_whole_files():
    # move only entire files if there is space to fit the entire file, starting
    # with highest file id
    defragged = [0] * files[0][1]
    file_ids = sorted(files.keys(), reverse=True)
    for file_id in file_ids:
        fitting_free_blocks = sorted([k for k in free_spaces.keys() if k >= files[file_id][1]])
        if not fitting_free_blocks: continue
        # if there is a free space of the same size or bigger as the file
        if len(free_spaces[fitting_free_blocks[0]]) > 0:
            # check that the free space is to the left of current position
            if not files[file_id][0] > free_spaces[fitting_free_blocks[0]][0]:
                continue
            # change the location of the file and remove that free space
            new_block_position = free_spaces[fitting_free_blocks[0]].pop(0)
            files[file_id][0] = new_block_position
            # if the free block still exists, and has just been made smaller,
            # we have to update our free spaces
            free_size_diff = fitting_free_blocks[0] - files[file_id][1]
            if free_size_diff:
                free_spaces[free_size_diff].append(new_block_position + files[file_id][1])
                free_spaces[free_size_diff] = sorted(free_spaces[free_size_diff])
    answer = 0
    for k, v in files.items():
        for i in range(v[0], v[0] + v[1]):
            answer += k * i
    return answer



start_time = time()
print(f'Part 2 answer: {defrag_whole_files()}')
print(f'Runtime: {time() - start_time}')
