from collections import Counter

from aoc.util import load_input, load_example


def propose_move(elves: set, position: tuple, round: int):
    #    print('position', position)
    x, y = position
    N = x, y - 1
    S = x, y + 1
    W = x - 1, y
    E = x + 1, y
    NE = x + 1, y - 1
    NW = x - 1, y - 1
    SE = x + 1, y + 1
    SW = x - 1, y + 1
    # If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
    if not elves.intersection((N, S, W, E, NE, NW, SE, SW)):
        return position
    for i in range(4):
        # If there is no Elf in the N, NE, NW adjacent positions, the Elf proposes moving north one step.
        if (i + round) % 4 == 0 and not elves.intersection((N, NE, NW)):
            return N
        # If there is no Elf in the S, SE, SW adjacent positions, the Elf proposes moving south one step.
        if (i + round) % 4 == 1 and not elves.intersection((S, SE, SW)):
            return S
        # If there is no Elf in the W, NW, SW adjacent positions, the Elf proposes moving west one step.
        if (i + round) % 4 == 2 and not elves.intersection((W, NW, SW)):
            return W
        # If there is no Elf in the E, NE, SE adjacent positions, the Elf proposes moving east one step.
        if (i + round) % 4 == 3 and not elves.intersection((E, NE, SE)):
            return E
    return position


def propose_moves(elves: set, round: int):
    print("elves", elves)
    proposals = {}
    for position in elves:
        target = propose_move(elves, position, round)
        proposals[position] = target
    print(proposals)
    return proposals


def move(proposals: dict):
    """proposals = {from1: to1, from2: to2, ...}"""
    valid_targets = [to for to, count in Counter(proposals.values()).items() if count == 1]
    #    print('valid_targets', valid_targets)
    next_elves = set()
    for position, target in proposals.items():
        if target in valid_targets:
            next_elves.add(target)
        else:
            next_elves.add(position)
    return next_elves


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    110
    """
    elves = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "#":
                elves.add((x, y))
    #   print(elves)
    for y in range(-2, 10):
        for x in range(-2, 9):
            if (x, y) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()

    for round in range(10):
        proposals = propose_moves(elves, round)
        elves = move(proposals)
        for y in range(-2, 10):
            for x in range(-2, 9):
                if (x, y) in elves:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    #   print(elves)
    max_x = max(x for x, _ in elves)
    min_x = min(x for x, _ in elves)
    max_y = max(y for _, y in elves)
    min_y = min(y for _, y in elves)
    print(max_x, min_x, max_y, min_y)
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    .
    """
    ...


if __name__ == "__main__":
    # data = load_input(__file__, 2022, "23")
    data = load_example(__file__, "23")
    # print(part1(data))
    print(part2(data))
