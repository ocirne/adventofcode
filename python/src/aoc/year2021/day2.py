from aoc.util import load_input, load_example


def extract(lines, word):
    result = []
    for line in lines:
        cmd, num = line.split()
        if cmd == word:
            result.append(int(num))
    return result


def part1(lines):
    down = sum(extract(lines, "down"))
    forward = sum(extract(lines, "forward"))
    up = sum(extract(lines, "up"))
    return forward * (down - up)


def part2(lines):
    hor = 0
    dep = 0
    aim = 0
    for line in lines:
        cmd, num = line.split()
        x = int(num)
        if cmd == "down":
            aim += x
        if cmd == "up":
            aim -= x
        if cmd == "forward":
            hor += x
            dep += aim * x
    return hor * dep


if __name__ == "__main__":
    data = load_input(__file__, 2021, "2")
    print(part1(data))
    print(part2(data))
