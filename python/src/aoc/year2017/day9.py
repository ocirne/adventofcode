from aoc.util import load_input


def run(stream):
    i = 0
    depth = 0
    garbage = False
    count_garbage = 0
    count_groups = 0
    while i < len(stream):
        c = stream[i]
        i += 1
        if c == "!":
            i += 1
            continue
        if c == ">":
            garbage = False
        if garbage:
            count_garbage += 1
            continue
        if c == "<":
            garbage = True
        if c == "{":
            depth += 1
        if c == "}":
            count_groups += depth
            depth -= 1
    return count_groups, count_garbage


def total_score(stream):
    """
    >>> total_score('{}')
    1
    >>> total_score('{{{}}}')
    6
    >>> total_score('{{},{}}')
    5
    >>> total_score('{{{},{},{{}}}}')
    16
    >>> total_score('{<a>,<a>,<a>,<a>}')
    1
    >>> total_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    9
    >>> total_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    9
    >>> total_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')
    3
    """
    return run(stream)[0]


def count_garbage(stream):
    """
    >>> count_garbage('<>')
    0
    >>> count_garbage('<random characters>')
    17
    >>> count_garbage('<<<<>')
    3
    >>> count_garbage('<{!>}>')
    2
    >>> count_garbage('<!!>')
    0
    >>> count_garbage('<!!!>>')
    0
    >>> count_garbage('<{o"i!a,<{i<a>')
    10
    """
    return run(stream)[1]


def part1(lines):
    return total_score(lines[0].strip())


def part2(lines):
    return count_garbage(lines[0].strip())


if __name__ == "__main__":
    data = load_input(__file__, 2017, "9")
    print(part1(data))
    print(part2(data))
