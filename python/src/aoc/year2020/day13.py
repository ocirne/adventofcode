from aoc.util import example


def prepare_data(lines):
    n = int(next(lines))
    ids = [int(x) for x in filter(lambda x: x != 'x', next(lines).strip().split(','))]
    return n, ids


def search(n, bus_ids):
    wait = 0
    while True:
        for bus_id in bus_ids:
            if (n+wait) % bus_id == 0:
                return wait * bus_id
        wait += 1


def part1(lines):
    """
    >>> part1(example(__file__, '13'))
    295
    """
    n, ids = prepare_data(lines)
    return search(n, ids)
