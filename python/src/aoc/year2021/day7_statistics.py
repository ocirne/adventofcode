from aoc.util import load_input, load_example

from statistics import median, mean


def move_cost1(initial_position, align_position):
    return abs(align_position - initial_position)


def move_cost2(initial_position, align_position):
    d = abs(align_position - initial_position)
    return int(d * (d + 1) / 2)


def calculate_fuel(move_cost, positions, align_position):
    return sum(move_cost(p, align_position) for p in positions)


def loop(lines, move_cost, circa):
    initial_positions = list(map(int, lines[0].split(",")))
    middle = int(circa(initial_positions))
    return min(calculate_fuel(move_cost, initial_positions, i) for i in range(middle - 1, middle + 2))


def part1(lines):
    """
    >>> part1(load_example(__file__, "7"))
    37
    """
    return loop(lines, move_cost1, median)


def part2(lines):
    """
    >>> part2(load_example(__file__, "7"))
    168
    """
    return loop(lines, move_cost2, mean)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "7")
    print(part1(data))
    print(part2(data))
