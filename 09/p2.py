import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip()

files = dict()
spaces = []

id = 0
pos = 0

for i in range(len(input)):
    n = int(input[i])
    if i % 2 == 0:
        files[id] = (pos, n)
        id += 1
    else:
        if n != 0:
            spaces.append((pos, n))
    pos += n


while id > 0:
    id -= 1
    file_pos, file_size = files[id]
    for i, (space_pos, space_size) in enumerate(spaces):
        if space_pos >= file_pos:
            spaces = spaces[:i]
            break
        if file_size <= space_size:
            files[id] = (space_pos, file_size)
            if file_size == space_size:
                spaces.pop(i)
            else:
                spaces[i] = (space_pos + file_size, space_size - file_size)
            break

result = 0

for id in files:
    pos, size = files[id]
    for x in range(pos, pos + size):
        result += id * x

print(result)
