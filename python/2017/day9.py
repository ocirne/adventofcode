
def run(stream):
    i = 0
    depth = 0
    garbage = False
    count_garbage = 0
    count_groups = 0
    while i < len(stream):
        c = stream[i]
        i += 1
        if c == '!':
            i += 1
            continue
        if c == '>':
            garbage = False
        if garbage:
            count_garbage += 1
            continue
        if c == '<':
            garbage = True
        if c == '{':
            depth += 1
        if c == '}':
            count_groups += depth
            depth -= 1
    return count_groups, count_garbage


def part1(stream):
    """
    >>> part1('{}')
    1
    >>> part1('{{{}}}')
    6
    >>> part1('{{},{}}')
    5
    >>> part1('{{{},{},{{}}}}')
    16
    >>> part1('{<a>,<a>,<a>,<a>}')
    1
    >>> part1('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    9
    >>> part1('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    9
    >>> part1('{{<a!>},{<a!>},{<a!>},{<ab>}}')
    3
    """
    return run(stream)[0]


def part2(stream):
    """
    >>> part2('<>')
    0
    >>> part2('<random characters>')
    17
    >>> part2('<<<<>')
    3
    >>> part2('<{!>}>')
    2
    >>> part2('<!!>')
    0
    >>> part2('<!!!>>')
    0
    >>> part2('<{o"i!a,<{i<a>')
    10
    """
    return run(stream)[1]


if __name__ == '__main__':
    input_data = open('input').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
