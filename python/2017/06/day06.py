from pathlib import Path


def redistribute(banks):
    value = max(banks)
    index = banks.index(value)
    result = list(banks)
    result[index] = 0
    for i in range(value):
        result[(index + 1 + i) % len(banks)] += 1
    return tuple(result)


def run(filename):
    """
    >>> run(Path(__file__).parent / 'reference')
    5
    """
    banks = tuple(int(line) for line in open(filename, 'r').readline().split())
    known = set()
    count = 1
    while True:
#        print(banks)
        banks = redistribute(banks)
        if banks in known:
            return count
        known.add(banks)
        count += 1


if __name__ == '__main__':
    assert run('reference') == 5
    print(run('input'))
