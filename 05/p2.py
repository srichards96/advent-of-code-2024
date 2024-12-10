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


def correct_update_order(not_before_rules: dict[int, set[int]], updates: list[int]):
    i = 0
    while i < len(updates):
        next_i = i + 1

        if updates[i] in not_before_rules:
            not_before_rules_for_i = not_before_rules[updates[i]]

            # Check previous "updates" in list.
            for j in range(i):
                # If update[j] shouldn't be before update[i]...
                if updates[j] in not_before_rules_for_i:
                    # Swap them, and revalidate all updates from index j
                    updates[i], updates[j] = updates[j], updates[i]
                    next_i = j
                    break

        i = next_i

    return updates


# Read and process "updates"
corrected_middle_page_sum = 0
for i in range(split_index + 1, len(input)):
    updates = list(map(lambda s: int(s), input[i].split(",")))

    if not is_update_valid(not_before_rules, updates):
        corrected_updates = correct_update_order(not_before_rules, updates)
        corrected_middle_page_sum += corrected_updates[len(corrected_updates) // 2]

print(corrected_middle_page_sum)
