from collections import Counter

from aoc.util import load_input


def extract(line):
    """
    >>> extract('1-3 a: abcde')
    (1, 3, 'a', 'abcde')
    """
    pw_range, pw_letter, pw_password = line.split()
    first, second = map(int, pw_range.split("-"))
    letter = pw_letter.split(":")[0]
    return first, second, letter, pw_password


def is_valid_part1(line):
    """
    >>> is_valid_part1('1-3 a: abcde')
    True
    >>> is_valid_part1('1-3 b: cdefg')
    False
    >>> is_valid_part1('2-9 c: ccccccccc')
    True
    """
    first, second, letter, password = extract(line)
    counter = Counter(password)
    count_letter = int(counter[letter])
    return first <= count_letter <= second


def is_valid_part2(line):
    """
    >>> is_valid_part2('1-3 a: abcde')
    True
    >>> is_valid_part2('1-3 b: cdefg')
    False
    >>> is_valid_part2('2-9 c: ccccccccc')
    False
    """
    first, second, letter, password = extract(line)
    count = 0
    if password[first - 1] == letter:
        count += 1
    if password[second - 1] == letter:
        count += 1
    return count == 1


def run(lines, is_valid):
    return sum(is_valid(line) for line in lines)


def part1(lines):
    return run(lines, is_valid_part1)


def part2(lines):
    return run(lines, is_valid_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2020, "2")
    print(part1(data))
    print(part2(data))
