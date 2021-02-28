from aoc.util import load_example, load_input
from sage.all import CRT_list


def wrap_crt(line):
    """
    >>> wrap_crt('17,x,13,19')
    3417
    >>> wrap_crt('67,7,59,61')
    754018
    >>> wrap_crt('67,x,7,59,61')
    779210
    >>> wrap_crt('67,7,x,59,61')
    1261476
    >>> wrap_crt('1789,37,47,1889')
    1202161486
    """
    ids = line.split(',')
    values = []
    moduli = []
    for i in range(len(ids)):
        if ids[i] == 'x':
            continue
        v = int(ids[i])
        values.append(v)
        moduli.append(v - i)
    return CRT_list(moduli, values)


def part2(lines):
    """
    >>> part2(load_example('13b'))
    1068781
    """
    return wrap_crt(lines[1].strip())


if __name__ == "__main__":
    data = load_input(__file__, 2020, '13')
    print(part2(data))
