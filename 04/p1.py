import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")

MAX_X = len(input[0]) - 1
MAX_Y = len(input) - 1

xmas_count = 0
for y in range(MAX_Y + 1):
    for x in range(MAX_X + 1):
        if input[y][x] != "X":
            continue

        can_go_right = (x + 3) <= MAX_X
        can_go_left = (x - 3) >= 0
        can_go_down = (y + 3) <= MAX_Y
        can_go_up = (y - 3) >= 0

        if can_go_right:
            if (
                input[y][x + 1] == "M"
                and input[y][x + 2] == "A"
                and input[y][x + 3] == "S"
            ):
                xmas_count += 1

        if can_go_right and can_go_down:
            if (
                input[y + 1][x + 1] == "M"
                and input[y + 2][x + 2] == "A"
                and input[y + 3][x + 3] == "S"
            ):
                xmas_count += 1

        if can_go_down:
            if (
                input[y + 1][x] == "M"
                and input[y + 2][x] == "A"
                and input[y + 3][x] == "S"
            ):
                xmas_count += 1

        if can_go_left and can_go_down:
            if (
                input[y + 1][x - 1] == "M"
                and input[y + 2][x - 2] == "A"
                and input[y + 3][x - 3] == "S"
            ):
                xmas_count += 1

        if can_go_left:
            if (
                input[y][x - 1] == "M"
                and input[y][x - 2] == "A"
                and input[y][x - 3] == "S"
            ):
                xmas_count += 1

        if can_go_left and can_go_up:
            if (
                input[y - 1][x - 1] == "M"
                and input[y - 2][x - 2] == "A"
                and input[y - 3][x - 3] == "S"
            ):
                xmas_count += 1

        if can_go_up:
            if (
                input[y - 1][x] == "M"
                and input[y - 2][x] == "A"
                and input[y - 3][x] == "S"
            ):
                xmas_count += 1

        if can_go_right and can_go_up:
            if (
                input[y - 1][x + 1] == "M"
                and input[y - 2][x + 2] == "A"
                and input[y - 3][x + 3] == "S"
            ):
                xmas_count += 1

print(xmas_count)
