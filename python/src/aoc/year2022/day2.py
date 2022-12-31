from aoc.util import load_input, load_example

mapping = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

# opponent, me -> result
result = {
    ("R", "R"): 3,
    ("R", "P"): 6,
    ("R", "S"): 0,
    ("P", "R"): 0,
    ("P", "P"): 3,
    ("P", "S"): 6,
    ("S", "R"): 6,
    ("S", "P"): 0,
    ("S", "S"): 3,
}

score_shape = {"R": 1, "P": 2, "S": 3}


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    15
    """
    res = 0
    for line in lines:
        if not line:
            continue
        opponent, me = line.split()
        o = mapping[opponent]
        m = mapping[me]
        r = result[(o, m)]
        s = score_shape[m] + r
        res += s
    return res


mapping2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


# opponent, me -> result
result2 = {
    ("R", 3): "R",
    ("R", 6): "P",
    ("R", 0): "S",
    ("P", 0): "R",
    ("P", 3): "P",
    ("P", 6): "S",
    ("S", 6): "R",
    ("S", 0): "P",
    ("S", 3): "S",
}


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    12
    """
    res = 0
    for line in lines:
        if not line:
            continue
        opponent, me = line.split()
        o = mapping[opponent]
        m = mapping2[me]
        r = result2[(o, m)]
        s = score_shape[r] + m
        res += s
    return res


if __name__ == "__main__":
    data = load_input(__file__, 2022, "2")
    print(part1(data))
    print(part2(data))
