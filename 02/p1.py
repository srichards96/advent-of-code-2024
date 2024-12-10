import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")


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


safeCount = 0

for line in input:
    levels = list(map(lambda s: int(s), line.split(" ")))

    if isSafe(levels):
        safeCount += 1

print(safeCount)
