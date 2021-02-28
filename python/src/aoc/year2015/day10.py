from aoc.util import load_input


def step(seq):
    """
    >>> step('1')
    '11'
    >>> step('11')
    '21'
    >>> step('21')
    '1211'
    >>> step('1211')
    '111221'
    >>> step('111221')
    '312211'
    """
    result = ''
    count = 0
    c = lc = seq[0]
    for c in seq:
        if c == lc:
            count += 1
        else:
            result += str(count) + lc
            count = 1
            lc = c
    result += str(count) + c
    return result


def play_look_and_say(start_seq, rounds):
    seq = start_seq
    for i in range(rounds):
        seq = step(seq)
    return len(seq)


def part1(lines):
    start_seq = lines[0]
    return play_look_and_say(start_seq, 40)


def part2(lines):
    start_seq = lines[0]
    return play_look_and_say(start_seq, 50)


if __name__ == "__main__":
    data = load_input(__file__, 2015, '10')
    print(part1(data))
    print(part2(data))
