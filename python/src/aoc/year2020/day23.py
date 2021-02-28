from aoc.util import load_input


def prepare_part1(data):
    values = list(map(int, data))
    result = {values[len(values)-1]: values[0]}
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    return result


def prepare_part2(data):
    m = 10**6
    values = list(map(int, data))
    result = list(range(m+1))
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    result[values[len(values)-1]] = 10
    for i in range(11, m+1):
        result[i-1] = i
    result[m] = values[0]
    return result


def dec(t, m):
    if t == 1:
        return m
    return t - 1


def answer_part1(d):
    result = ''
    i = 1
    while d[i] != 1:
        result += str(d[i])
        i = d[i]
    return result


def answer_part2(d):
    return d[1] * d[d[1]]


def run(data, rounds, m, prepare_data, collect_answer):
    """
    >>> run('389125467', 10, 9, prepare_part1, answer_part1)
    '92658374'
    >>> run('389125467', 100, 9, prepare_part1, answer_part1)
    '67384529'
    >>> run('389125467', 10**7, 10**6, prepare_part2, answer_part2)
    149245887792
    """
    d = prepare_data(data)
    current = int(data[0])
    for _ in range(rounds):
        # pick three
        one = d[current]
        second = d[one]
        third = d[second]
        fourth = d[third]
        # identify next smaller number
        t = dec(current, m)
        while t in [one, second, third]:
            t = dec(t, m)
        # reorder
        d[current], d[t], d[third] = fourth, one, d[t]
        # next current
        current = d[current]
    return collect_answer(d)


def part1(lines):
    line = lines[0].strip()
    return run(line, 100, 9, prepare_part1, answer_part1)


def part2(lines):
    line = lines[0].strip()
    return run(line, 10**7, 10**6, prepare_part2, answer_part2)


if __name__ == "__main__":
    data = load_input(__file__, 2020, '23')
    print(part1(data))
    print(part2(data))
