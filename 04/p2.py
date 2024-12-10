import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")

MAX_X = len(input[0]) - 1
MAX_Y = len(input) - 1

x_mas_count = 0
for y in range(MAX_Y + 1):
    for x in range(MAX_X + 1):
        if input[y][x] != "A":
            continue

        # Check all 4 corners are inbounds
        if not ((x - 1) >= 0 and (x + 1) <= MAX_X):
            continue
        if not ((y - 1) >= 0 and (y + 1) <= MAX_Y):
            continue

        tl = input[y - 1][x - 1]
        br = input[y + 1][x + 1]
        if not (tl == "M" and br == "S" or tl == "S" and br == "M"):
            continue

        bl = input[y + 1][x - 1]
        tr = input[y - 1][x + 1]
        if not (bl == "M" and tr == "S" or bl == "S" and tr == "M"):
            continue

        x_mas_count += 1


print(x_mas_count)
