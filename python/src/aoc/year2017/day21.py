from collections import Counter

from aoc.util import load_input, load_example

START = ".#./..#/###"
SIZES = {5: 2, 11: 3}


def j(field):
    return "/".join(field)


def flip(field):
    return j(line[::-1] for line in field.split("/"))


def rotate(field):
    """
    >>> rotate('#./..')
    '.#/..'
    >>> rotate('.#/..')
    '../.#'
    >>> rotate('../.#')
    '../#.'
    >>> rotate('../#.')
    '#./..'
    """
    size = SIZES[len(field)]
    lines = field.split("/")
    result = ""
    for x in range(size):
        for y in range(size):
            result += lines[size - 1 - y][x]
        if x < size - 1:
            result += "/"
    return result


def gen_rotate_flip(in_pat):
    field = in_pat
    for i in range(4):
        yield field
        yield flip(field)
        field = rotate(field)


def prepare_rules(lines):
    rules = {}
    for line in lines:
        in_pat, out_pat = line.strip().split(" => ")
        for in_pat_rf in gen_rotate_flip(in_pat):
            if in_pat_rf in rules:
                if out_pat != rules[in_pat_rf]:
                    raise
            else:
                rules[in_pat_rf] = out_pat
    return rules


def step(rules, grid):
    field = grid.split("/")
    if len(field[0]) % 2 == 0:
        i_size = 2
    else:
        i_size = 3
    o_size = len(field[0]) // i_size
    result = ["" for _ in range(o_size * (i_size + 1))]
    for oy in range(o_size):
        for ox in range(o_size):
            in_cell = ""
            for iy in range(i_size):
                for ix in range(i_size):
                    in_cell += field[i_size * oy + iy][i_size * ox + ix]
                if iy < i_size - 1:
                    in_cell += "/"
            out_cell = rules[in_cell].split("/")
            for iy in range(i_size + 1):
                for ix in range(i_size + 1):
                    result[(i_size + 1) * oy + iy] += out_cell[iy][ix]
    return j(result)


def run(lines, iterations):
    """
    >>> run(load_example(__file__, "21"), 2)
    12
    """
    rules = prepare_rules(lines)
    grid = START
    for i in range(iterations):
        grid = step(rules, grid)
    return Counter(grid)["#"]


def part1(lines):
    return run(lines, 5)


def part2(lines):
    return run(lines, 18)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "21")
    print(part1(data))
    print(part2(data))
