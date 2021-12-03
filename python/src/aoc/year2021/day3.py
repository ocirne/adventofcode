from collections import Counter

from aoc.util import load_input, load_example

MOST_COMMON = 0
LEAST_COMMON = 1


def find_common(values, pos, preference, i):
    mc = Counter(line[i] for line in values).most_common()
    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        return preference
    return mc[pos][0]


def column_counts(lines, pos):
    return "".join(find_common(lines, pos, None, i) for i in range(len(lines[0].strip())))


def part1(lines):
    """
    >>> part1(load_example(__file__, "3"))
    198
    """
    gamma = int(column_counts(lines, MOST_COMMON), 2)
    epsilon = int(column_counts(lines, LEAST_COMMON), 2)
    return gamma * epsilon


def determine(values, position, preference, i=0):
    if len(values) == 1:
        return values
    mc = find_common(values, position, preference, i)
    filtered_values = [value for value in values if value[i] == mc]
    return determine(filtered_values, position, preference, i + 1)


def part2(lines):
    """
    >>> part2(load_example(__file__, "3"))
    230
    """
    values = [line.strip() for line in lines]
    oxygen = determine(values, MOST_COMMON, preference="1")
    assert len(oxygen) == 1
    co2 = determine(values, LEAST_COMMON, preference="0")
    assert len(co2) == 1
    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "3")
    print(part1(data))
    print(part2(data))
