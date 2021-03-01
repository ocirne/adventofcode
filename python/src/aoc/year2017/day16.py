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


def part1(lines, initial_standing="abcdefghijklmnop"):
    """
    >>> part1(load_example(__file__, "16"), "abcde")
    'baedc'
    """
    standing = list(initial_standing)
    for cmd in lines[0].strip().split(","):
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
    return "".join(standing)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "16")
    print(part1(data))
#    print(part1(load_example(__file__, "16"), "abcde"))
