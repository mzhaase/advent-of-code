# free space 
free_spaces = []
files = []

input = open('./input').read().strip()

block_index = 0
file_id     = 0
for idx, char in enumerate(input):
    if not idx%2:
        files.append({
            'index': block_index,
            'id': file_id,
            'size': int(char)
        })
        file_id += 1
    else:
        free_spaces.append({
            'index': block_index,
            'size': int(char)
        })
    block_index += int(char)

for file_index in range(len(files) - 1, 0, -1):
    # we are going backwards through all files and then forwards through all
    # free spaces, and place the file in the first free space
    for free_space_index in range(len(free_spaces)):
        # otherwise we can "move" files to the right
        if free_spaces[free_space_index]['index'] > files[file_index]['index']:
            continue
        size_diff = free_spaces[free_space_index]['size'] - files[file_index]['size']
        if size_diff >= 0:
            files[file_index]['index'] = free_spaces[free_space_index]['index']
            free_spaces[free_space_index]['size'] = size_diff
            if size_diff > 0:
                free_spaces[free_space_index]['index'] += files[file_index]['size']
            break

answer = 0
for file in files:
    for i in range(file['size']):
        answer += (i + file['index']) * file['id']
print(answer)