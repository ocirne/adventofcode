from collections import Counter
from pathlib import Path


def count_adjacent_occupied_part1(y, x, d):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if 0 <= (y+dy) < len(d) and 0 <= (x+dx) < len(d[0]) and d[y+dy][x+dx] == '#':
                count += 1
    return count


def calc_next_state_part1(y, x, d):
    if d[y][x] == 'L':
        if count_adjacent_occupied_part1(y, x, d) == 0:
            return '#'
    elif d[y][x] == '#':
        if count_adjacent_occupied_part1(y, x, d) >= 4:
            return 'L'
    return d[y][x]


def step_part1(d):
    result = []
    changed = False
    for y in range(len(d)):
        line = d[y]
        result.append('')
        for x in range(len(line)):
            next_state = calc_next_state_part1(y, x, d)
            result[y] += next_state
            if next_state != d[y][x]:
                changed = True
    return changed, result


def count_seats(d):
    c = Counter(''.join(d))
    return c['#']


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    37
    """
    f = open(filename)
    d = list(map(str.strip, f.readlines()))
    changed = True
    while changed:
        changed, d = step_part1(d)
    return count_seats(d)


def count_adjacent_occupied_part2(y, x, d):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            distance = 1
            ry = y + (distance*dy)
            rx = x + (distance*dx)
            while 0 <= ry < len(d) and 0 <= rx < len(d[0]):
                if d[ry][rx] == '#':
                    count += 1
                    break
                elif d[ry][rx] == 'L':
                    break
                distance += 1
                ry = y + (distance*dy)
                rx = x + (distance*dx)
    return count


def calc_next_state_part2(y, x, d):
    if d[y][x] == 'L':
        if count_adjacent_occupied_part2(y, x, d) == 0:
            return '#'
    elif d[y][x] == '#':
        if count_adjacent_occupied_part2(y, x, d) >= 5:
            return 'L'
    return d[y][x]


def step_part2(d):
    result = []
    changed = False
    for y in range(len(d)):
        line = d[y]
        result.append('')
        for x in range(len(line)):
            next_state = calc_next_state_part2(y, x, d)
            result[y] += next_state
            if next_state != d[y][x]:
                changed = True
    return changed, result


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    26
    """
    f = open(filename)
    d = list(map(str.strip, f.readlines()))
    changed = True
    while changed:
        changed, d = step_part2(d)
    return count_seats(d)


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
