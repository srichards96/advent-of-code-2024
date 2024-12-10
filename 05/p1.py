import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip().split("\n")

split_index = input.index("")

# Read "rules" up to first empty line
# Maps from number (n) to set of numbers which cannot appear before it
not_before_rules = dict[int, set[int]]()
for i in range(split_index):
    x, y = map(lambda s: int(s), input[i].split("|"))

    if not x in not_before_rules:
        not_before_rules[x] = set()
    not_before_rules[x].add(y)  # y cannot appear before x

    i += 1


def is_update_valid(not_before_rules: dict[int, set[int]], updates: list[int]):
    for i in range(len(updates)):
        if updates[i] in not_before_rules:
            not_before_rules_for_i = not_before_rules[updates[i]]

            # Check previous "updates" in list.
            for j in range(i):
                if updates[j] in not_before_rules_for_i:
                    return False

    return True


# Read and process "updates"
middle_page_sum = 0
for i in range(split_index + 1, len(input)):
    updates = list(map(lambda s: int(s), input[i].split(",")))

    if is_update_valid(not_before_rules, updates):
        middle_page_sum += updates[len(updates) // 2]

print(middle_page_sum)
