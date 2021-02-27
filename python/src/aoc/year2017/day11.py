
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


def count_steps(line):
    """
    >>> count_steps("ne,ne,ne")
    3
    >>> count_steps("ne,ne,sw,sw")
    0
    >>> count_steps("ne,ne,s,s")
    2
    >>> count_steps("se,sw,se,sw,sw")
    3
    """
    return run(line)[0]


def max_distance(line):
    return run(line)[1]


def part1(lines):
    return count_steps(lines[0].strip())


def part2(lines):
    return max_distance(lines[0].strip())
