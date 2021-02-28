from collections import Counter

from aoc.util import load_input, load_example


def endpoint(line, x=0, y=0):
    """
    >>> endpoint('nwwswee')
    (0, 0)
    """
    if line == "":
        return x, y
    if line.startswith("nw"):
        return endpoint(line[2:], x, y - 1)
    if line.startswith("ne"):
        return endpoint(line[2:], x + 1, y - 1)
    if line.startswith("sw"):
        return endpoint(line[2:], x - 1, y + 1)
    if line.startswith("se"):
        return endpoint(line[2:], x, y + 1)
    if line.startswith("w"):
        return endpoint(line[1:], x - 1, y)
    if line.startswith("e"):
        return endpoint(line[1:], x + 1, y)
    else:
        raise Exception


def prepare_endpoints(lines):
    return (endpoint(line.strip()) for line in lines)


def part1(lines):
    """
    >>> part1(load_example(__file__, '24'))
    10
    """
    endpoints = prepare_endpoints(lines)
    return sum(1 for v in Counter(endpoints).values() if v % 2 == 1)


def count_env(endpoints, x, y):
    result = 0
    if (x, y - 1) in endpoints:
        result += 1
    if (x + 1, y - 1) in endpoints:
        result += 1
    if (x - 1, y + 1) in endpoints:
        result += 1
    if (x, y + 1) in endpoints:
        result += 1
    if (x - 1, y) in endpoints:
        result += 1
    if (x + 1, y) in endpoints:
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


def part2(lines, rounds=100):
    """
    >>> data = load_example(__file__, '24')
    >>> part2(data, 0)
    10
    >>> part2(data, 1)
    15
    >>> part2(data, 2)
    12
    >>> part2(data, 3)
    25
    >>> part2(data, 4)
    14
    >>> part2(data, 5)
    23
    >>> part2(data, 6)
    28
    >>> part2(data, 7)
    41
    >>> part2(data, 8)
    37
    >>> part2(data, 9)
    49
    >>> part2(data, 10)
    37
    >>> part2(data, 20)
    132
    >>> part2(data, 30)
    259
    >>> part2(data, 40)
    406
    >>> part2(data, 50)
    566
    >>> part2(data, 60)
    788
    >>> part2(data, 70)
    1106
    >>> part2(data, 80)
    1373
    >>> part2(data, 90)
    1844
    >>> part2(data, 100)
    2208
    """
    endpoints = prepare_endpoints(lines)
    real_endpoints = {ep: True for ep, count in Counter(endpoints).items() if count % 2 == 1}
    return simulate(real_endpoints, rounds)


if __name__ == "__main__":
    data = load_input(__file__, 2020, "24")
    print(part1(data))
    print(part2(data))
