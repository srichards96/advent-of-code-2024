import os


def readInputFile():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "input.txt")

    with open(filename) as file:
        return file.read().replace("\n", "")


def part1():
    sum = 0

    # To length -7 since mul(x,y) needs at least 8 chars
    i = 0
    input = readInputFile()
    while i < len(input) - 7:
        if input[i : i + 4] == "mul(":
            i += 4

            # Try to read 1st number
            if not input[i].isdigit():
                continue

            number_1 = 0
            while input[i].isdigit():
                number_1 = number_1 * 10 + int(input[i])
                i += 1

            # Check for comma
            if not input[i] == ",":
                continue
            i += 1

            # Try to read 2nd number
            if not input[i].isdigit():
                continue

            number_2 = 0
            while input[i].isdigit():
                number_2 = number_2 * 10 + int(input[i])
                i += 1

            # Check for closing parenthesis
            if not input[i] == ")":
                continue

            sum += number_1 * number_2

        i += 1

    return sum


def part2():
    sum = 0

    # To length -7 since mul(x,y) needs at least 8 chars
    i = 0
    input = readInputFile()
    do = True
    while i < len(input) - 7:
        if input[i : i + 4] == "do()":
            do = True
        if input[i : i + 7] == "don't()":
            do = False
        if do and input[i : i + 4] == "mul(":
            i += 4

            # Try to read 1st number
            if not input[i].isdigit():
                continue

            number_1 = 0
            while input[i].isdigit():
                number_1 = number_1 * 10 + int(input[i])
                i += 1

            # Check for comma
            if not input[i] == ",":
                continue
            i += 1

            # Try to read 2nd number
            if not input[i].isdigit():
                continue

            number_2 = 0
            while input[i].isdigit():
                number_2 = number_2 * 10 + int(input[i])
                i += 1

            # Check for closing parenthesis
            if not input[i] == ")":
                continue

            sum += number_1 * number_2

        i += 1

    return sum


print(part1())
print(part2())
