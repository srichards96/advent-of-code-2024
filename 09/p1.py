import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip()

disk: list[int] = []
id = 0

for i in range(len(input)):
    n = int(input[i])
    if i % 2 == 0:
        disk.extend([id] * n)
        id += 1
    else:
        disk.extend([-1] * n)

space_indices = [i for i, v in enumerate(disk) if v == -1]

for i in space_indices:
    while disk[-1] == -1:
        disk.pop()

    if i >= len(disk):
        break
    disk[i] = disk.pop()

print(sum([i * v for i, v in enumerate(disk)]))
