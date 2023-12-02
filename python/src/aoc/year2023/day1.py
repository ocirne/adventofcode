from aoc.util import load_input, load_example

DIGITS = {str(n): str(n) for n in range(1, 10)}

DIGITS_AND_WORDS = DIGITS.copy()
DIGITS_AND_WORDS.update(
    {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
)


def concat_first_last(line, numbers):
    first = last = None
    min_index, max_index = len(line), -1
    for n, d in numbers.items():
        left_index = line.find(n)
        if left_index == -1:
            continue
        if left_index < min_index:
            min_index = left_index
            first = d
        right_index = line.rfind(n)
        if right_index > max_index:
            max_index = right_index
            last = d
    return int(first + last)


def part1(lines):
    """
    >>> part1(load_example(__file__, "1a"))
    142
    """
    return sum(concat_first_last(line, DIGITS) for line in lines)


def part2(lines):
    """
    >>> part2(load_example(__file__, "1b"))
    281
    """
    return sum(concat_first_last(line, DIGITS_AND_WORDS) for line in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "1")
    print(part1(data))
    print(part2(data))
