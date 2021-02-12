from math import sqrt


def get_edge_length(target):
    result = int(sqrt(target))
    if result % 2 == 0:
        result -= 1
    if result**2 == target:
        return result
    return result + 2


def manhattan_distance(x, y, middle):
    return abs(x-middle) + abs(y-middle)


def coordinates(edge, target):
    bottom_right = edge**2
    bottom_left = bottom_right - (edge-1)
    top_left = bottom_left - (edge-1)
    top_right = top_left - (edge-1)
    x = y = edge-1
    if bottom_right == target:
        return x, y
    if bottom_left <= target < bottom_right:
        x = target - bottom_left
        return x, y
    else:
        x = 0
    if top_left <= target < bottom_left:
        y = target - top_left
        return x, y
    else:
        y = 0
    if top_right <= target < top_left:
        x = top_left - target
        return x, y
    else:
        x = edge-1
    y = top_right - target
    return x, y


def part1(target):
    """
    >>> part1(1)
    0
    >>> part1(12)
    3
    >>> part1(23)
    2
    >>> part1(1024)
    31
    """
    edge = get_edge_length(target)
    middle = (edge-1) // 2
    x, y = coordinates(edge, target)
    return manhattan_distance(x, y, middle)


if __name__ == '__main__':
    inputData = int(open('input', 'r').readline())
    print(part1(inputData))
#    print(part2(inputData))
