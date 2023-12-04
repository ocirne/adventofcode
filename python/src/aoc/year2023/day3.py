from collections import defaultdict

from aoc.util import load_input, load_example


def is_symbol(d, y, x):
    if y < 0 or len(d) <= y:
        return False
    if x < 0 or len(d[y]) <= x:
        return False
    c = d[y][x]
    return not (c.isdigit() or c == ".")


def detect_adjacent_symbol(d):
    part_number = ""
    symbol_positions = []
    for y in range(len(d)):
        for x in range(len(d[y])):
            c = d[y][x]
            if not part_number and c.isdigit():
                # start of a number
                symbol_positions.extend(
                    (sy, sx)
                    for sy, sx in ((y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y - 1, x), (y + 1, x))
                    if is_symbol(d, sy, sx)
                )
                part_number += c
            elif part_number and c.isdigit():
                # in a number
                symbol_positions.extend((sy, sx) for sy, sx in ((y - 1, x), (y + 1, x)) if is_symbol(d, sy, sx))
                part_number += c
            elif part_number and not c.isdigit():
                # end of a number
                symbol_positions.extend((sy, sx) for sy, sx in ((y - 1, x), (y, x), (y + 1, x)) if is_symbol(d, sy, sx))
                if symbol_positions:
                    yield int(part_number), symbol_positions
                part_number = ""
                symbol_positions = []
        if part_number:
            # end of a number on a line
            if symbol_positions:
                yield int(part_number), symbol_positions
            part_number = ""
            symbol_positions = []


def part1(lines):
    """
    >>> part1(load_example(__file__, "3"))
    4361
    """
    return sum(n for n, _ in detect_adjacent_symbol(lines))


def part2(lines):
    """
    >>> part2(load_example(__file__, "3"))
    467835
    """
    m = defaultdict(list)
    for n, symbol_positions in detect_adjacent_symbol(lines):
        for gy, gx in symbol_positions:
            if lines[gy][gx] == "*":
                m[gy, gx].append(n)
    return sum(n[0] * n[1] for n in m.values() if len(n) == 2)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "3")
    print(part1(data))
    print(part2(data))
