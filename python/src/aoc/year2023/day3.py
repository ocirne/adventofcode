from collections import defaultdict

from aoc.util import load_input, load_example


def is_symbol(d, y, x):
    if y < 0 or len(d) <= y:
        return False
    if x < 0 or len(d[y]) <= x:
        return False
    c = d[y][x]
    return not (c.isdigit() or c == ".")


def detect_part_numbers(d):
    part_number = ""
    part_flag = False
    for y in range(len(d)):
        for x in range(len(d[y])):
            c = d[y][x]
            if not part_number and c.isdigit():
                # start of a number
                if is_symbol(d, y - 1, x - 1) or is_symbol(d, y, x - 1) or is_symbol(d, y + 1, x - 1):
                    part_flag = True
                if is_symbol(d, y - 1, x) or is_symbol(d, y + 1, x):
                    part_flag = True
                part_number += c
            elif part_number and c.isdigit():
                # in a number
                if is_symbol(d, y - 1, x) or is_symbol(d, y + 1, x):
                    part_flag = True
                part_number += c
            elif part_number and not c.isdigit():
                # end of a number
                if is_symbol(d, y - 1, x) or is_symbol(d, y, x) or is_symbol(d, y + 1, x):
                    part_flag = True
                if part_flag:
                    yield int(part_number)
                part_number = ""
                part_flag = False
        if part_number:
            # end of a number on a line
            if part_flag:
                yield int(part_number)
            part_number = ""
            part_flag = False


def part1(lines):
    """
    >>> part1(load_example(__file__, "3"))
    4361
    """
    return sum(detect_part_numbers(lines))


def is_gear(d, y, x):
    if y < 0 or len(d) <= y:
        return False
    if x < 0 or len(d[y]) <= x:
        return False
    return d[y][x] == "*"


def detect_gear_numbers(d):
    part_number = ""
    gear_pos = None
    for y in range(len(d)):
        for x in range(len(d[y])):
            c = d[y][x]
            if not part_number and c.isdigit():
                # start of a number
                for gy, gx in ((y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y - 1, x), (y + 1, x)):
                    if is_gear(d, gy, gx):
                        gear_pos = gy, gx
                part_number += c
            elif part_number and c.isdigit():
                # in a number
                for gy, gx in ((y - 1, x), (y + 1, x)):
                    if is_gear(d, gy, gx):
                        gear_pos = gy, gx
                part_number += c
            elif part_number and not c.isdigit():
                # end of a number
                for gy, gx in ((y - 1, x), (y, x), (y + 1, x)):
                    if is_gear(d, gy, gx):
                        gear_pos = gy, gx
                if gear_pos is not None:
                    yield int(part_number), gear_pos
                part_number = ""
                gear_pos = None
        if part_number:
            # end of a number on a line
            if gear_pos is not None:
                yield int(part_number), gear_pos
            part_number = ""
            gear_pos = None


def part2(lines):
    """
    >>> part2(load_example(__file__, "3"))
    467835
    """
    m = defaultdict(list)
    for n, gear_pos in detect_gear_numbers(lines):
        m[gear_pos].append(n)
    return sum(n[0] * n[1] for n in m.values() if len(n) == 2)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "3")
    print(part1(data))
    print(part2(data))
