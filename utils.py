import os


def readInputFile():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "input.txt")

    with open(filename) as file:
        return file.read().split("\n")
