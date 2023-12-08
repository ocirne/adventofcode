from aoc.util import load_input, load_example
import re

NETWORK_PATTERN = r"(\w{3}) = \((\w{3}), (\w{3})\)"


def part1(lines):
    """
    >>> part1(load_example(__file__, "8a"))
    2
    >>> part1(load_example(__file__, "8b"))
    6
    """
    instructions = [0 if d == "L" else 1 for d in lines[0].strip()]
    network = {}
    for line in lines[2:]:
        node, right, left = re.match(NETWORK_PATTERN, line).groups()
        network[node] = (right, left)
    p = "AAA"
    i = 0
    while p != "ZZZ":
        p = network[p][instructions[i % len(instructions)]]
        i += 1
    return i


def part2(lines):
    """
    >>> part2(load_example(__file__, "8"))

    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "8")
    print(part1(data))
#   print(part2(data))
