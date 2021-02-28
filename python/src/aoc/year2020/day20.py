from collections import Counter
from math import prod
from aoc.util import load_example, load_input


def extract_number(s):
    return int(s.replace("#", "1").replace(".", "0"), 2)


def extract_borders(field):
    return [
        extract_number(field[0]),
        extract_number(field[-1]),
        extract_number("".join(line[0] for line in field)),
        extract_number("".join(line[-1] for line in field)),
        extract_number(field[0][::-1]),
        extract_number(field[-1][::-1]),
        extract_number("".join(line[0] for line in field)[::-1]),
        extract_number("".join(line[-1] for line in field)[::-1]),
    ]


def prepare_tiles(lines):
    tiles = {}
    current_number = None
    for line in lines:
        if line.isspace():
            continue
        elif line.startswith("Tile"):
            current_number = line.split(" ")[1].split(":")[0]
            tiles[current_number] = []
        else:
            tiles[current_number].append(line.strip())
    return tiles


def part1(lines):
    """
    >>> part1(load_example(__file__, '20'))
    20899048083289
    """
    tiles = prepare_tiles(lines)
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
    corner_keys = [
        int(key) for key, value in Counter(unique_keys).items() if value == 4
    ]
    return prod(corner_keys)


def part2(lines):
    """ TODO """
    pass


if __name__ == "__main__":
    data = load_input(__file__, 2020, "20")
    print(part1(data))
    print(part2(data))
