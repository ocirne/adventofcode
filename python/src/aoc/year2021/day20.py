from collections import defaultdict, Counter

from aoc.util import load_input, load_example

TO_NUMBER = {".": "0", "#": "1"}


def get_index(old_lights, fx, fy, tx, ty):
    return int("".join(TO_NUMBER[old_lights[x, y]] for y in range(fy, ty) for x in range(fx, tx)), 2)


def step(old_lights, img_enh_algo, min_x, min_y, max_x, max_y):
    if img_enh_algo[0] == "." or old_lights[10000, 10000] == "#":
        new_lights = defaultdict(lambda: ".")
    else:
        new_lights = defaultdict(lambda: "#")
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            index = get_index(old_lights, x - 1, y - 1, x + 2, y + 2)
            new_lights[x, y] = img_enh_algo[index]
    return new_lights


def enhance_image(lines, steps):
    img_enh_algo = lines[0].strip()
    lights = defaultdict(lambda: ".")
    max_x = len(lines[2])
    max_y = len(lines)
    min_x = -1
    min_y = -1
    lights.update({(x, y): light for y, line in enumerate(lines[2:]) for x, light in enumerate(line.strip())})
    for i in range(steps):
        lights = step(lights, img_enh_algo, min_x - i, min_y - i, max_x + i, max_y + i)
    return Counter(lights.values())["#"]


def part1(lines):
    """
    >>> part1(load_example(__file__, "20"))
    35
    """
    return enhance_image(lines, 2)


def part2(lines):
    """
    >>> part2(load_example(__file__, "20"))
    3351
    """
    return enhance_image(lines, 50)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "20")
    print(part1(data))
    print(part2(data))
