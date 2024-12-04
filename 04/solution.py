import os


def readInputFile():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "input.txt")

    with open(filename) as file:
        return file.read()


def part1():
    xmas_count = 0

    lines = [line for line in readInputFile().split("\n") if line != ""]

    row_count = len(lines)
    for y in range(0, row_count):
        col_count = len(lines[y])
        for x in range(0, col_count):
            if lines[y][x] != "X":
                continue

            can_go_right = (x + 3) < col_count
            can_go_left = (x - 3) >= 0
            can_go_down = (y + 3) < row_count
            can_go_up = (y - 3) >= 0

            if can_go_right:
                if (
                    lines[y][x + 1] == "M"
                    and lines[y][x + 2] == "A"
                    and lines[y][x + 3] == "S"
                ):
                    xmas_count += 1

            if can_go_right and can_go_down:
                if (
                    lines[y + 1][x + 1] == "M"
                    and lines[y + 2][x + 2] == "A"
                    and lines[y + 3][x + 3] == "S"
                ):
                    xmas_count += 1

            if can_go_down:
                if (
                    lines[y + 1][x] == "M"
                    and lines[y + 2][x] == "A"
                    and lines[y + 3][x] == "S"
                ):
                    xmas_count += 1

            if can_go_left and can_go_down:
                if (
                    lines[y + 1][x - 1] == "M"
                    and lines[y + 2][x - 2] == "A"
                    and lines[y + 3][x - 3] == "S"
                ):
                    xmas_count += 1

            if can_go_left:
                if (
                    lines[y][x - 1] == "M"
                    and lines[y][x - 2] == "A"
                    and lines[y][x - 3] == "S"
                ):
                    xmas_count += 1

            if can_go_left and can_go_up:
                if (
                    lines[y - 1][x - 1] == "M"
                    and lines[y - 2][x - 2] == "A"
                    and lines[y - 3][x - 3] == "S"
                ):
                    xmas_count += 1

            if can_go_up:
                if (
                    lines[y - 1][x] == "M"
                    and lines[y - 2][x] == "A"
                    and lines[y - 3][x] == "S"
                ):
                    xmas_count += 1

            if can_go_right and can_go_up:
                if (
                    lines[y - 1][x + 1] == "M"
                    and lines[y - 2][x + 2] == "A"
                    and lines[y - 3][x + 3] == "S"
                ):
                    xmas_count += 1

    return xmas_count


def part2():
    x_mas_count = 0

    lines = [line for line in readInputFile().split("\n") if line != ""]

    row_count = len(lines)
    for y in range(0, row_count):
        col_count = len(lines[y])
        for x in range(0, col_count):
            if lines[y][x] != "A":
                continue

            # Check all 4 corners are inbounds
            if not (x > 0 and (x + 1) < col_count):
                continue
            if not (y > 0 and (y + 1) < row_count):
                continue

            tl = lines[y - 1][x - 1]
            br = lines[y + 1][x + 1]
            if not (tl == "M" and br == "S" or tl == "S" and br == "M"):
                continue

            bl = lines[y + 1][x - 1]
            tr = lines[y - 1][x + 1]
            if not (bl == "M" and tr == "S" or bl == "S" and tr == "M"):
                continue

            x_mas_count += 1

    return x_mas_count


print(part1())
print(part2())
