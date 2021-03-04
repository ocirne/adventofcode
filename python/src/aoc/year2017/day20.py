from aoc.util import load_input


def part1(lines):
    return next(index for index, line in enumerate(lines) if "a=<0,0,0>" in line)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "20")
    print(part1(data))
