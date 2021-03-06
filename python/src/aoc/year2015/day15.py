from aoc.util import load_example, load_input


def prepare_data(lines):
    result = []
    for line in lines:
        result.append([int(ingredient.split()[1]) for ingredient in line.split(":")[1].split(",")])
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


def run(lines, p, calories_condition=False):
    """
    >>> run(load_example(__file__, '15'), 2, False)
    62842880
    >>> run(load_example(__file__, '15'), 2, True)
    57600000
    """
    data = prepare_data(lines)
    return max(apply(data, part, calories_condition) for part in partitions(100, p))


def part1(lines):
    return run(lines, 4, calories_condition=False)


def part2(lines):
    return run(lines, 4, calories_condition=True)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "15")
    print(part1(data))
    print(part2(data))
