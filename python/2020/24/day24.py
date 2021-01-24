from collections import Counter
from pathlib import Path


def endpoint(line, x=0, y=0):
    """
    >>> endpoint('nwwswee')
    (0, 0)
    """
    if line == '':
        return x, y
    if line.startswith('nw'):
        return endpoint(line[2:], x, y-1)
    if line.startswith('ne'):
        return endpoint(line[2:], x+1, y-1)
    if line.startswith('sw'):
        return endpoint(line[2:], x-1, y+1)
    if line.startswith('se'):
        return endpoint(line[2:], x, y+1)
    if line.startswith('w'):
        return endpoint(line[1:], x-1, y)
    if line.startswith('e'):
        return endpoint(line[1:], x+1, y)
    else:
        raise Exception


def read_endpoints(filename):
    f = open(filename, 'r')
    return (endpoint(line.strip()) for line in f.readlines())


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    10
    """
    endpoints = read_endpoints(filename)
    return sum(1 for v in Counter(endpoints).values() if v % 2 == 1)


def count_env(endpoints, x, y):
    result = 0
    if (x, y-1) in endpoints:
        result += 1
    if (x+1, y-1) in endpoints:
        result += 1
    if (x-1, y+1) in endpoints:
        result += 1
    if (x, y+1) in endpoints:
        result += 1
    if (x-1, y) in endpoints:
        result += 1
    if (x+1, y) in endpoints:
        result += 1
    return result


def simulate_round(old_endpoints):
    result = {}
    min_x = min(x for x, _ in old_endpoints) - 1
    max_x = max(x for x, _ in old_endpoints) + 2
    min_y = min(y for _, y in old_endpoints) - 1
    max_y = max(y for _, y in old_endpoints) + 2
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            count = count_env(old_endpoints, x, y)
            if (x, y) in old_endpoints:
                if not (count == 0 or count > 2):
                    result[(x, y)] = True
            else:
                if count == 2:
                    result[(x, y)] = True
    return result


def simulate(para_endpoints, rounds):
    endpoints = para_endpoints
    for _ in range(rounds):
        endpoints = simulate_round(endpoints)
    return len(endpoints)


def part2(filename, rounds):
    """
    >>> part2(Path(__file__).parent / 'reference', 0)
    10
    >>> part2(Path(__file__).parent / 'reference', 1)
    15
    >>> part2(Path(__file__).parent / 'reference', 2)
    12
    >>> part2(Path(__file__).parent / 'reference', 3)
    25
    >>> part2(Path(__file__).parent / 'reference', 4)
    14
    >>> part2(Path(__file__).parent / 'reference', 5)
    23
    >>> part2(Path(__file__).parent / 'reference', 6)
    28
    >>> part2(Path(__file__).parent / 'reference', 7)
    41
    >>> part2(Path(__file__).parent / 'reference', 8)
    37
    >>> part2(Path(__file__).parent / 'reference', 9)
    49
    >>> part2(Path(__file__).parent / 'reference', 10)
    37
    >>> part2(Path(__file__).parent / 'reference', 20)
    132
    >>> part2(Path(__file__).parent / 'reference', 30)
    259
    >>> part2(Path(__file__).parent / 'reference', 40)
    406
    >>> part2(Path(__file__).parent / 'reference', 50)
    566
    >>> part2(Path(__file__).parent / 'reference', 60)
    788
    >>> part2(Path(__file__).parent / 'reference', 70)
    1106
    >>> part2(Path(__file__).parent / 'reference', 80)
    1373
    >>> part2(Path(__file__).parent / 'reference', 90)
    1844
    >>> part2(Path(__file__).parent / 'reference', 100)
    2208
    """
    endpoints = read_endpoints(filename)
    real_endpoints = {ep: True for ep, count in Counter(endpoints).items() if count % 2 == 1}
    return simulate(real_endpoints, rounds)


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input', 100))
