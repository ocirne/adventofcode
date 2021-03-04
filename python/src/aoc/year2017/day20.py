from aoc.util import load_input


def part1(lines):
    r""" ¯\_(ツ)_/¯ """
    return next(index for index, line in enumerate(lines) if "a=<0,0,0>" in line)


def part2(lines):
    pass


if __name__ == "__main__":
    data = load_input(__file__, 2017, "20")
    print(part1(data))
