from pathlib import Path


def read_data(filename):
    result = []
    f = open(filename, 'r')
    for line in f.readlines():
        result.append([int(ingredient.split()[1]) for ingredient in line.split(':')[1].split(',')])
    return result


def partitions(total, count, acc=None):
    if acc is None:
        acc = []
    if count == 1:
        yield acc + [total]
    else:
        for i in range(1, total):
            for p in partitions(total - i, count - 1, acc + [i]):
                yield p


def apply(data, part, calories_condition=False):
    if calories_condition and sum(data[j][4] * part[j] for j in range(len(part))) != 500:
        return 0
    result = 1
    for i in range(4):
        x = sum(data[j][i] * part[j] for j in range(len(part)))
        if x <= 1:
            return 0
        result *= x
    return result


def run(filename, p, calories_condition=False):
    """
    >>> run(Path(__file__).parent / 'reference', 2, False)
    62842880
    >>> run(Path(__file__).parent / 'reference', 2, True)
    57600000
    """
    data = read_data(filename)
    return max(apply(data, part, calories_condition) for part in partitions(100, p))


if __name__ == '__main__':
    print(run('input', 4, calories_condition=False))
    print(run('input', 4, calories_condition=True))
