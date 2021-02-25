from pathlib import Path
from sage.all import CRT_list


def read_data(filename):
    f = open(filename)
    f.readline()
    return f.readline().strip()


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


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    1068781
    """
    return wrap_crt(read_data(filename))


if __name__ == '__main__':
    print(part2('input'))
