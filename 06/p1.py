import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    grid = list(map(lambda s: list(s), file.read().strip().split("\n")))

MAX_Y = len(grid) - 1
MAX_X = len(grid[0]) - 1


def find_guard():
    dir_chars = "^>v<"

    for y in range(MAX_Y + 1):
        for x in range(MAX_X + 1):
            char = grid[y][x]
            if char in dir_chars:
                return (x, y, dir_chars.index(char))

    raise "No guard exists!"


dir_changes = [
    [0, -1],  # 0 - UP    -  x   , y-1
    [1, 0],  #  1 - RIGHT -  x+1 , y
    [0, 1],  #  2 - DOWN  -  x   , y+1
    [-1, 0],  # 3 - LEFT  -  x-1 , y
]

x, y, dir = find_guard()
visited: set[tuple[int, int]] = set()

# Assumes grid contains no loops and guard will eventually move out-of-bounds...
while True:
    visited.add((x, y))

    next_x = x + dir_changes[dir][0]
    next_y = y + dir_changes[dir][1]

    if next_x < 0 or next_x > MAX_X:
        break
    if next_y < 0 or next_y > MAX_Y:
        break

    if grid[next_y][next_x] == "#":
        dir = (dir + 1) % 4
    else:
        x = next_x
        y = next_y

print(len(visited))
