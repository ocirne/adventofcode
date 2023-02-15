from aoc.util import load_input, load_example

base_a = ord("a") - 1
base_A = ord("A") - 27


def common_item(line):
    """
    >>> common_item("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    >>> common_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    'L'
    >>> common_item("PmmdzqPrVvPwwTWBwg")
    'P'
    >>> common_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    'v'
    >>> common_item("ttgJtRGJQctTZtZT")
    't'
    >>> common_item("CrZsJsPPZsGzwwsLwLmpwMDw")
    's'
    """
    s = len(line) // 2
    first, second = line[:s], line[s:]
    return set(first).intersection(set(second)).pop()


def priority(item: str):
    """
    >>> priority("a")
    1
    >>> priority("z")
    26
    >>> priority("A")
    27
    >>> priority("Z")
    52
    """
    if item.islower():
        return ord(item) - base_a
    elif item.isupper():
        return ord(item) - base_A
    else:
        raise


def part1(lines):
    """
    >>> part1(load_example(__file__, "3"))
    157
    """
    return sum(priority(common_item(line)) for line in lines)


def chunks(lines: list):
    while lines:
        yield lines.pop(), lines.pop(), lines.pop()


def common_badge(f, s, t):
    """
    >>> common_badge("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg")
    'r'
    >>> common_badge("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw")
    'Z'
    """
    return set(f).intersection(set(s)).intersection(set(t)).pop()


def part2(lines):
    """
    >>> part2(load_example(__file__, "3"))
    70
    """
    return sum(priority(common_badge(*badges)) for badges in chunks(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2022, "3")
    print(part1(data))
    print(part2(data))
