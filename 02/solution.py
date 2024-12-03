import os


def readInputFile():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "input.txt")

    with open(filename) as file:
        return file.read()


def isSafe(levels: list[int]):
    onlyIncreases = True
    onlyDecreases = True

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        onlyIncreases &= diff > 0
        onlyDecreases &= diff < 0

        if not (onlyIncreases or onlyDecreases):
            return False

        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True


def isSafeWithLevelRemoved(levels: list[int], indexToRemove: int):
    withoutLevelAtIndex = [x for i, x in enumerate(levels) if i != indexToRemove]
    return isSafe(withoutLevelAtIndex)


def isSafeWith1Skip(levels: list[int]):
    if isSafe(levels):
        return True

    safe = False

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]

        # Diff too big - see if levels become valid without 1 of them
        if abs(diff) < 1 or abs(diff) > 3:
            safe |= isSafeWithLevelRemoved(levels, i - 1)
            safe |= isSafeWithLevelRemoved(levels, i)
            break  # Only check once

        if i + 1 < len(levels):
            diffAhead = levels[i + 1] - levels[i]
            # Diff changed direction - see if levels become valid without prev, curr, or next
            if (diff > 0) != (diffAhead > 0):
                safe |= isSafeWithLevelRemoved(levels, i - 1)
                safe |= isSafeWithLevelRemoved(levels, i)
                safe |= isSafeWithLevelRemoved(levels, i + 1)
                break  # Only check once

    return safe


def part1():
    safeCount = 0

    input = readInputFile()
    for line in input.split("\n"):
        levels = list(map(lambda s: int(s), line.split(" ")))

        if isSafe(levels):
            safeCount += 1

    return safeCount


def part2():
    safeCount = 0

    input = readInputFile()
    for line in input.split("\n"):
        levels = list(map(lambda s: int(s), line.split(" ")))

        if isSafeWith1Skip(levels):
            safeCount += 1

    return safeCount


print(part1())
print(part2())
