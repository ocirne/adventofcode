
TRANSLATE = {
    'nw': lambda x, y: (x - 1, y),
    'se': lambda x, y: (x + 1, y),
    'ne': lambda x, y: (x + 1, y - 1),
    'sw': lambda x, y: (x - 1, y + 1),
    'n': lambda x, y: (x, y - 1),
    's': lambda x, y: (x, y + 1),
}


def distance(x, y):
    return max(abs(y), abs(x), abs(x+y))


def run(data):
    x = y = md = 0
    for step in data.split(','):
        x, y = TRANSLATE[step](x, y)
        md = max(md, distance(x, y))
    return distance(x, y), md


def part1(data):
    """
    >>> part1("ne,ne,ne")
    3
    >>> part1("ne,ne,sw,sw")
    0
    >>> part1("ne,ne,s,s")
    2
    >>> part1("se,sw,se,sw,sw")
    3
    """
    return run(data)[0]


def part2(data):
    return run(data)[1]


if __name__ == '__main__':
    input_data = open('input', 'r').readline().strip()
    print(part1(input_data))
    print(part2(input_data))
