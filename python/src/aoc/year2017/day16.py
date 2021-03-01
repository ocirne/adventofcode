from aoc.util import load_input, load_example


def spin(s, param):
    v = -int(param)
    return s[v:] + s[:v]


def exchange(s, param):
    px, py = (int(i) for i in param.split("/"))
    s[px], s[py] = s[py], s[px]
    return s


def partner(s, param):
    x, y = param.split("/")
    i = s.index(x)
    j = s.index(y)
    s[i], s[j] = s[j], s[i]
    return s


COMMANDS = {
    "s": spin,
    "x": exchange,
    "p": partner,
}


def dance(commands, initial_standing):
    standing = initial_standing
    for cmd in commands:
        fun = COMMANDS[cmd[0]]
        standing = fun(standing, cmd[1:])
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
