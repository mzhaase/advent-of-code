from copy import deepcopy
from time import time as time

# input is a long int. alternatingly the numbers represent the length of a file
# and length of free space.
# we create two lists: one that represents if a block is free and taken, and a 
# second list with the file_ids of those blocks. ids start at 0 and increment

debug = True
file_id = 0
none_count = 0
file_ids = []
with open('./sample', 'r') as f:
    chars = []
    for line in f:
        for char in line.strip():
            chars.append(int(char))
for idx, char in enumerate(chars):
    for i in range(char):
        # this means it is in an even position (0,2,4), and therefore, a file
        if not idx%2:
            file_ids.append(file_id)
        else:
            file_ids.append(None)
            none_count += 1
    if not idx%2:
        file_id += 1

def defrag():
    # move blocks to the leftmost free block, compute checksum which is
    # file_id * block_index
    tmp_ids = deepcopy(file_ids)
    defragged = []
    answer = 0
    for i in range(len(file_ids) - none_count):
        if not file_ids[i] == None:
            if debug: defragged.append(file_ids[i])
            answer += i * file_ids[i]
        else:
            _ = None
            while _ == None:
                _ = tmp_ids.pop()
            if debug: defragged.append(_)
            answer += i * _
    if debug: print(defragged)
    return answer


start_time = time()
print(f'Part 1 answer: {defrag()}')
print(f'Runtime: {time() - start_time}')