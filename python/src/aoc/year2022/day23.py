from collections import Counter

from aoc.util import load_input, load_example


def contains_any(elves: set, items):
    return any(item in elves for item in items)


def propose_move(elves: set, position: tuple, r: int):
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
    if not contains_any(elves, (N, S, W, E, NE, NW, SE, SW)):
        return position
    for i in range(4):
        # If there is no Elf in the N, NE, NW adjacent positions, the Elf proposes moving north one step.
        if (i + r) % 4 == 0 and not contains_any(elves, (N, NE, NW)):
            return N
        # If there is no Elf in the S, SE, SW adjacent positions, the Elf proposes moving south one step.
        if (i + r) % 4 == 1 and not contains_any(elves, (S, SE, SW)):
            return S
        # If there is no Elf in the W, NW, SW adjacent positions, the Elf proposes moving west one step.
        if (i + r) % 4 == 2 and not contains_any(elves, (W, NW, SW)):
            return W
        # If there is no Elf in the E, NE, SE adjacent positions, the Elf proposes moving east one step.
        if (i + r) % 4 == 3 and not contains_any(elves, (E, NE, SE)):
            return E
    return position


def propose_moves(elves: set, r: int):
    return {position: propose_move(elves, position, r) for position in elves}


def move(proposals: dict):
    """proposals = {from1: to1, from2: to2, ...}"""
    valid_targets = [to for to, count in Counter(proposals.values()).items() if count == 1]
    return set((target if target in valid_targets else position) for position, target in proposals.items())


def move_elves(lines, is_part1):
    elves = set((x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#")
    r = 0
    while True:
        proposals = propose_moves(elves, r)
        if is_part1 and r == 10:
            max_x = max(x for x, _ in elves)
            min_x = min(x for x, _ in elves)
            max_y = max(y for _, y in elves)
            min_y = min(y for _, y in elves)
            return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
        r += 1
        moved_elves = [(f, t) for f, t in proposals.items() if f != t]
        if not moved_elves:
            return r
        elves = move(proposals)


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    110
    """
    return move_elves(lines, is_part1=True)


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    20
    """
    return move_elves(lines, is_part1=False)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "23")
    print(part1(data))
    print(part2(data))
