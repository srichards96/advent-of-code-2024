import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")


left: list[int] = []
right: dict[int, int] = dict()

for line in input:
    l, r = map(lambda s: int(s), line.split("   "))
    left.append(l)

    if r not in right:
        right[r] = 0
    right[r] += 1

similarity = 0

for l in left:
    if l in right:
        similarity += l * right[l]

print(similarity)
