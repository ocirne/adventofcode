from pathlib import Path


def read_data(filename):
    f = open(filename)
    n = int(f.readline())
    ids = [int(x) for x in filter(lambda x: x != 'x', f.readline().strip().split(','))]
    return n, ids


def search(n, bus_ids):
    wait = 0
    while True:
        for bus_id in bus_ids:
            if (n+wait) % bus_id == 0:
                return wait * bus_id
        wait += 1


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    295
    """
    n, ids = read_data(filename)
    return search(n, ids)


if __name__ == '__main__':
    print(part1('input'))
