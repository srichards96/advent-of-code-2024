import os


def readInputFile():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "input.txt")

    with open(filename) as file:
        return [line for line in file]


def part1():
    left: list[int] = []
    right: list[int] = []

    for line in readInputFile():
        l, r = line.replace("\n", "").split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    distance = 0

    for i in range(len(left)):
        distance += abs(left[i] - right[i])

    return distance


def part2():
    left: list[int] = []
    right: dict[int, int] = dict()

    for line in readInputFile():
        l, r = line.replace("\n", "").split("   ")
        left.append(int(l))

        rInt = int(r)
        if rInt not in right:
            right[rInt] = 0
        right[rInt] += 1

    similarity = 0

    for l in left:
        if l in right:
            similarity += l * right[l]

    return similarity


print(part1())
print(part2())
