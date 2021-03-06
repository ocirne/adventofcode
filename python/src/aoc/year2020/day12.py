from aoc.util import load_example, load_input


def step_part1(pos_x, pos_y, face, action, value):
    dx, dy, df = 0, 0, 0
    if action == "N":
        dy = -value
    if action == "W":
        dx = -value
    if action == "S":
        dy = value
    if action == "E":
        dx = value
    if action == "R":
        df = -value
    if action == "L":
        df = value
    if action == "F":
        if face == 0:
            dx = value
        elif face == 90:
            dy = -value
        elif face == 180:
            dx = -value
        elif face == 270:
            dy = value
        else:
            raise Exception
    return pos_x + dx, pos_y + dy, (face + df + 360) % 360


def part1(lines):
    """
    >>> part1(load_example(__file__, '12'))
    25
    """
    pos_x, pos_y, face = 0, 0, 0
    for line in lines:
        action, value = line[0], int(line[1:])
        pos_x, pos_y, face = step_part1(pos_x, pos_y, face, action, int(value))
    return abs(pos_x) + abs(pos_y)


def rotate(x, y, degree):
    count = ((degree + 360) % 360) // 90
    for i in range(count):
        x, y = -y, x
    return x, y


def step_part2(pos_x, pos_y, way_x, way_y, face, action, value):
    dx, dy, nwx, nwy, df = 0, 0, way_x, way_y, 0
    if action == "N":
        nwy = way_y - value
    if action == "W":
        nwx = way_x - value
    if action == "S":
        nwy = way_y + value
    if action == "E":
        nwx = way_x + value
    if action == "R":
        nwx, nwy = rotate(way_x, way_y, value)
    if action == "L":
        nwx, nwy = rotate(way_x, way_y, -value)
    if action == "F":
        dx = value * way_x
        dy = value * way_y
    return pos_x + dx, pos_y + dy, nwx, nwy, (face + df + 360) % 360


def part2(lines):
    """
    >>> part2(load_example(__file__, '12'))
    286
    """
    pos_x, pos_y, way_x, way_y, face = 0, 0, 10, -1, 0
    for line in lines:
        action, value = line[0], int(line[1:])
        pos_x, pos_y, way_x, way_y, face = step_part2(pos_x, pos_y, way_x, way_y, face, action, int(value))
    return abs(pos_x) + abs(pos_y)


if __name__ == "__main__":
    data = load_input(__file__, 2020, "12")
    print(part1(data))
    print(part2(data))
