from collections import Counter
from math import prod
from pathlib import Path


def extract_number(s):
    return int(s.replace('#', '1').replace('.', '0'), 2)


def extract_borders(field):
    return [
        extract_number(field[0]),
        extract_number(field[-1]),
        extract_number(''.join(line[0] for line in field)),
        extract_number(''.join(line[-1] for line in field)),
        extract_number(field[0][::-1]),
        extract_number(field[-1][::-1]),
        extract_number(''.join(line[0] for line in field)[::-1]),
        extract_number(''.join(line[-1] for line in field)[::-1])
    ]


def read_tiles(filename):
    f = open(filename)
    tiles = {}
    current_number = None
    for line in f.readlines():
        if line.isspace():
            continue
        elif line.startswith('Tile'):
            current_number = line.split(' ')[1].split(':')[0]
            tiles[current_number] = []
        else:
            tiles[current_number].append(line.strip())
    return tiles


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    20899048083289
    """
    tiles = read_tiles(filename)
    all_borders = {}
    plain_borders = []
    for key, field in tiles.items():
        borders = extract_borders(field)
        all_borders[key] = borders
        plain_borders.extend(borders)
    count_borders = Counter(plain_borders)
    unique_keys = []
    for border, count in count_borders.items():
        if count == 1:
            for key, fieldBorder in all_borders.items():
                if border in fieldBorder:
                    unique_keys.append(key)
    corner_keys = [int(key) for key, value in Counter(unique_keys).items() if value == 4]
    return prod(corner_keys)


def part2():
    """ TODO """
    pass


if __name__ == '__main__':
    print(part1('input'))
