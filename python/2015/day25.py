
BASE = 20151125
FACTOR = 252533
MOD = 33554393


def prepare_data(lines):
    token = lines[0].split()
    return int(token[15].strip(',')), int(token[17].strip('.'))


def calc_number_on(x, y):
    """
    >>> calc_number_on(1, 1)
    1
    >>> calc_number_on(2, 2)
    5
    >>> calc_number_on(6, 1)
    16
    >>> calc_number_on(1, 6)
    21
    >>> calc_number_on(4, 3)
    18
    >>> calc_number_on(3, 4)
    19
    """
    return 1 + ((y-1) * y + (x-1) * x) // 2 + x * (y-1)


def calc_manual_numbers(n):
    """
    >>> calc_manual_numbers(1)
    20151125
    >>> calc_manual_numbers(2)
    31916031
    >>> calc_manual_numbers(3)
    18749137
    >>> calc_manual_numbers(21)
    33511524
    """
    return (BASE * pow(FACTOR, n-1, MOD)) % MOD


def part1(lines):
    x, y = prepare_data(lines)
    return calc_manual_numbers(calc_number_on(x, y))
