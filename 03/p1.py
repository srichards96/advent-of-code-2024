import os

dir = os.path.dirname(__file__)
filename = os.path.join(dir, "input.txt")

with open(filename) as file:
    input = file.read().strip()

sum = 0

# To length -7 since mul(x,y) needs at least 8 chars
i = 0

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

print(sum)
