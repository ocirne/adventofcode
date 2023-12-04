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
        row = d[y]
        for x in range(len(row)):
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


def part2(lines):
    """
    >>> part2(load_example(__file__, "3"))
    """


if __name__ == "__main__":
    data = load_input(__file__, 2023, "3")
    print(part1(data))
    print(part2(data))
