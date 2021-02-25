
def part1(line):
    """
    >>> part1('>')
    2
    >>> part1('^>v<')
    4
    >>> part1('^v^v^v^v^v')
    2
    """
    x, y = 0, 0
    houses = {(0, 0): True}
    for d in line:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y -= 1
        elif d == 'v':
            y += 1
        else:
            raise
        houses[(x, y)] = True
    return len(houses)


def move(d, x, y):
    if d == '>':
        return x + 1, y
    elif d == '<':
        return x - 1, y
    elif d == '^':
        return x, y - 1
    elif d == 'v':
        return x, y + 1
    raise


def part2(line):
    """
    >>> part2('^v')
    3
    >>> part2('^>v<')
    3
    >>> part2('^v^v^v^v^v')
    11
    """
    sx, sy, rx, ry = 0, 0, 0, 0
    houses = {(0, 0): True}
    for index, d in enumerate(line):
        if index % 2 == 0:
            sx, sy = move(d, sx, sy)
            houses[(sx, sy)] = True
        else:
            rx, ry = move(d, rx, ry)
            houses[(rx, ry)] = True
    return len(houses)


if __name__ == '__main__':
    inputData = open('input').readline()
    print(part1(inputData))
    print(part2(inputData))
