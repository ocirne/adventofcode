from aoc.util import load_input

WRAPPING = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
GREATER_THAN_ITEMS = ["cats", "trees"]
FEWER_THAN_ITEMS = ["pomeranians", "goldfish"]


def prepare_data(lines):
    result = []
    for line in lines:
        _, things_part = line.split(": ", 1)
        things = {}
        for thing in things_part.split(", "):
            key, value = thing.split(": ")
            things[key] = int(value)
        result.append(things)
    return result


def can_be1(things):
    for key, value in WRAPPING.items():
        if key in things and value != things[key]:
            return False
    return True


def can_be2(things):
    for key, value in WRAPPING.items():
        if key in things:
            if key in GREATER_THAN_ITEMS:
                if value > things[key]:
                    return False
            elif key in FEWER_THAN_ITEMS:
                if value < things[key]:
                    return False
            else:
                if value != things[key]:
                    return False
    return True


def run(lines, can_be, exclude=None):
    data = prepare_data(lines)
    for sue_no, things in enumerate(data):
        if can_be(things):
            if sue_no + 1 == exclude:
                continue
            return sue_no + 1


def part1(lines):
    return run(lines, can_be1)


def part2(lines):
    answer1 = part1(lines)
    return run(lines, can_be2, answer1)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "16")
    print(part1(data))
    print(part2(data))
