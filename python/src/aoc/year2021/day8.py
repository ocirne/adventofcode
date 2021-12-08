from aoc.util import load_input, load_example


def part1(lines):
    """
    >>> part1(load_example(__file__, "8"))
    26
    """
    result = 0
    for line in lines:
        signal_pattern, output_values = line.strip().split("|")
        result += sum(1 for output_value in output_values.split() if len(output_value) in [2, 3, 4, 7])
    return result


def part2(lines):
    """
    >>> part2(load_example(__file__, "8"))
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2021, "8")
    print(part1(data))
    print(part2(data))
