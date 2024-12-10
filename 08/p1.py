import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")

MAX_X = len(input[0]) - 1
MAX_Y = len(input) - 1

# Find every antenna on map and store their coordinates in a dictionary grouped by symbol
antennas: dict[str, list[tuple[int, int]]] = dict()

for y in range(MAX_Y + 1):
    for x in range(MAX_X + 1):
        char = input[y][x]
        if char != ".":
            if not char in antennas:
                antennas[char] = []
            antennas[char].append((x, y))

antinodes: set[tuple[int, int]] = set()

for key in antennas:
    nodes = antennas[key]

    # Compare each node against every other node
    for i in range(len(nodes)):
        n1 = nodes[i]

        for j in range(i + 1, len(nodes)):
            n2 = nodes[j]

            # Get distance from n2 to n1
            dx = n2[0] - n1[0]
            dy = n2[1] - n1[1]

            # Get antinode postions (- from n1, + from n2)
            n1x2 = n1[0] - dx
            n1y2 = n1[1] - dy
            n2x2 = n2[0] + dx
            n2y2 = n2[1] + dy

            # Add antinodes if in-bounds
            if n1x2 >= 0 and n1x2 <= MAX_X and n1y2 >= 0 and n1y2 <= MAX_Y:
                antinodes.add((n1x2, n1y2))
            if n2x2 >= 0 and n2x2 <= MAX_X and n2y2 >= 0 and n2y2 <= MAX_Y:
                antinodes.add((n2x2, n2y2))


print(len(antinodes))
