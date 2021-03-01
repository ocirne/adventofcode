from aoc.util import load_input, load_example


def spin(s, v):
    return s[v:] + s[:v]


def exchange(s, px, py):
    s[int(px)], s[int(py)] = s[int(py)], s[int(px)]
    return s


def partner(s: str, x, y):
    i = s.index(x)
    j = s.index(y)
    s[i], s[j] = s[j], s[i]
    return s


def dance(commands, initial_standing):
    standing = initial_standing
    for cmd in commands:
        #  print(line, standing)
        if cmd[0] == "s":
            #     print('s')
            standing = spin(standing, -int(cmd[1:]))
        elif cmd[0] == "x":
            #    print('x')
            standing = exchange(standing, *cmd[1:].split("/"))
        elif cmd[0] == "p":
            #   print('p')
            standing = partner(standing, *cmd[1:].split("/"))
        else:
            raise
    return standing


def part1(lines, initial_standing="abcdefghijklmnop"):
    """
    >>> part1(load_example(__file__, "16"), "abcde")
    'baedc'
    """
    commands = lines[0].strip().split(",")
    standing = dance(commands, list(initial_standing))
    return "".join(standing)


def find_loop(commands, initial_standing):
    standing = list(initial_standing)
    cache = {}
    i = 0
    while True:
        s = "".join(standing)
        if s in cache:
            # works because cache[s] is 0
            return cache, i
        cache[s] = i
        standing = dance(commands, standing)
        i += 1


def part2(lines, initial_standing="abcdefghijklmnop", count_dances=10 ** 9):
    """
    >>> part2(load_example(__file__, "16"), "abcde", 10)
    'ceadb'
    """
    commands = lines[0].strip().split(",")
    cache, s = find_loop(commands, initial_standing)
    return list(cache.keys())[count_dances % s]


if __name__ == "__main__":
    data = load_input(__file__, 2017, "16")
    print(part1(data))
    print(part2(data))
