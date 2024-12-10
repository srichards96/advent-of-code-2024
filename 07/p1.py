import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")


def can_make_total(target: int, values: list[int]):
    if len(values) == 1:
        return values[0] == target

    last = values[-1]

    # Addition - if last is less than target...
    if target > last:
        # See if remaining values can make the difference
        if can_make_total(target - last, values[:-1]):
            return True
    # Multiplication - if last is a multiple of target...
    if target % last == 0:
        # See if remaining values can make the other multiple
        if can_make_total(target // last, values[:-1]):
            return True

    return False


result = 0

for line in input:
    parts = line.split(": ")
    target = int(parts[0])
    values = [int(x) for x in parts[1].split(" ")]

    if can_make_total(target, values):
        result += target

print(result)
