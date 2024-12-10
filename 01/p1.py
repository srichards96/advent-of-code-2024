import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")


left: list[int] = []
right: list[int] = []

for line in input:
    l, r = map(lambda s: int(s), line.split("   "))
    left.append(l)
    right.append(r)

left.sort()
right.sort()

distance = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
