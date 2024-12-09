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

start_x, start_y, start_dir = find_guard()
x, y, dir = start_x, start_y, start_dir
original_visited: set[tuple[int, int]] = set()

# Assumes grid contains no loops and guard will eventually move out-of-bounds...
while True:
    original_visited.add((x, y))

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


def will_loop(obstruction_x: int, obstruction_y: int):
    # Make position into an obstruction and then recalculate guard path
    if grid[obstruction_y][obstruction_x] == "#":
        return False
    grid[obstruction_y][obstruction_x] = "#"
    x, y, dir = start_x, start_y, start_dir

    loops = False
    visited: set[tuple[int, int, int]] = set()
    while True:
        if (x, y, dir) in visited:
            loops = True
            break

        visited.add((x, y, dir))

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

    # Remove added obstruction
    grid[obstruction_y][obstruction_x] = "."

    return loops


# For each state of the guard, add a obstruction in the next position and recalculate guard path from there
# A loop is encountered if one of the guard's previous states is reached
loop_obstructions = 0
for x, y in original_visited:
    # Skip guard starting position
    if x == start_x and y == start_y:
        continue
    if will_loop(x, y):
        loop_obstructions += 1

print(loop_obstructions)
