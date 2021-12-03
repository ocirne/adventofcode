from aoc.util import load_input


class Node:
    def __init__(self, tokens):
        self.name = tokens[0]
        self.size = int(tokens[1][:-1])
        self.used = int(tokens[2][:-1])
        self.avail = int(tokens[3][:-1])
        self.use_percent = int(tokens[4][:-1])


def part1(lines):
    nodes = [Node(line.split()) for line in lines[2:]]
    count_viable_pairs = 0
    for a in nodes:
        if a.used == 0:
            continue
        for b in nodes:
            if a == b:
                continue
            if a.used < b.avail:
                count_viable_pairs += 1
    return count_viable_pairs


if __name__ == "__main__":
    data = load_input(__file__, 2016, "22")
    print(part1(data))
#    print(part2(data))
