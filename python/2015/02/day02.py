
def extract(line):
    """
    >>> extract('1x2x3')
    [1, 2, 3]
    >>> extract('3x2x1')
    [1, 2, 3]
    """
    return sorted(map(int, line.split('x')))


def calc_wrapping_paper(line):
    """
    >>> calc_wrapping_paper('2x3x4')
    58
    >>> calc_wrapping_paper('1x1x10')
    43
    """
    h, l, w = extract(line)
    return 3*h*l + 2*h*w + 2*l*w


def calc_ribbon(line):
    """
    >>> calc_ribbon('2x3x4')
    34
    >>> calc_ribbon('1x1x10')
    14
    """
    h, l, w = extract(line)
    return 2*(h+l) + h*l*w


def fun_and_sum(filename, fun):
    data = open(filename, 'r').readlines()
    return sum(fun(line) for line in data)


if __name__ == '__main__':
    print(fun_and_sum('input', calc_wrapping_paper))
    print(fun_and_sum('input', calc_ribbon))
