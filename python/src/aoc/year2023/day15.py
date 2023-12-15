import re
from functools import reduce

from aoc.util import load_input, load_example


def aoc_hash(step: str):
    """
    >>> aoc_hash("rn=1")
    30
    >>> aoc_hash("cm-")
    253
    >>> aoc_hash("qp=3")
    97
    >>> aoc_hash("cm=2")
    47
    >>> aoc_hash("qp-")
    14
    >>> aoc_hash("pc=4")
    180
    >>> aoc_hash("ot=9")
    9
    >>> aoc_hash("ab=5")
    197
    >>> aoc_hash("pc-")
    48
    >>> aoc_hash("pc=6")
    214
    >>> aoc_hash("ot=7")
    231
    """
    return reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, step, 0)


def part1(lines):
    """
    >>> part1(load_example(__file__, "15"))
    1320
    """
    return sum(aoc_hash(step) for step in lines[0].split(","))


def focusing_power(boxes):
    return sum(
        box_number * slot_number * focal_length
        for box_number, box in enumerate(boxes, start=1)
        for slot_number, focal_length in enumerate(box.values(), start=1)
    )


def part2(lines):
    """
    >>> part2(load_example(__file__, "15"))
    145
    """
    boxes = [{} for _ in range(256)]
    for step in lines[0].split(","):
        label = re.split(r"[=-]", step)[0]
        box = aoc_hash(label)
        if "=" in step:
            focal_length = int(step.split("=")[1])
            boxes[box][label] = focal_length
        elif "-" in step and label in boxes[box]:
            boxes[box].pop(label)
    return focusing_power(boxes)


if __name__ == "__main__":
    data = load_input(__file__, 2023, "15")
    print(part1(data))
    print(part2(data))
