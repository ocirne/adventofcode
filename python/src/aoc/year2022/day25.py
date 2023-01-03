from aoc.util import load_input, load_example

snafu_int = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
int_snafu = {3: "=", 4: "-", 0: "0", 1: "1", 2: "2"}


def snafu_to_decimal(snafu):
    """
    >>> snafu_to_decimal("1")
    1
    >>> snafu_to_decimal("2")
    2
    >>> snafu_to_decimal("1=")
    3
    >>> snafu_to_decimal("1-")
    4
    >>> snafu_to_decimal("10")
    5
    >>> snafu_to_decimal("11")
    6
    >>> snafu_to_decimal("12")
    7
    >>> snafu_to_decimal("2=")
    8
    >>> snafu_to_decimal("2-")
    9
    >>> snafu_to_decimal("20")
    10
    >>> snafu_to_decimal("1=0")
    15
    >>> snafu_to_decimal("1-0")
    20
    >>> snafu_to_decimal("1=11-2")
    2022
    >>> snafu_to_decimal("1-0---0")
    12345
    >>> snafu_to_decimal("1121-1110-1=0")
    314159265
    """
    result = 0
    b = 1
    for c in reversed(snafu):
        result += b * snafu_int[c]
        b *= 5
    return result


def decimal_to_snafu(n):
    """
    >>> decimal_to_snafu(1)
    '1'
    >>> decimal_to_snafu(2)
    '2'
    >>> decimal_to_snafu(3)
    '1='
    >>> decimal_to_snafu(4)
    '1-'
    >>> decimal_to_snafu(5)
    '10'
    >>> decimal_to_snafu(6)
    '11'
    >>> decimal_to_snafu(7)
    '12'
    >>> decimal_to_snafu(8)
    '2='
    >>> decimal_to_snafu(9)
    '2-'
    >>> decimal_to_snafu(10)
    '20'
    >>> decimal_to_snafu(15)
    '1=0'
    >>> decimal_to_snafu(20)
    '1-0'
    >>> decimal_to_snafu(2022)
    '1=11-2'
    >>> decimal_to_snafu(12345)
    '1-0---0'
    >>> decimal_to_snafu(314159265)
    '1121-1110-1=0'
    """
    if n == 0:
        return "0"
    result = ""
    b = 5
    while n > 0:
        r = n % 5
        result = int_snafu[r] + result
        n = (n - r) // 5 + int(r >= 3)
        b *= 5
    return result


def part1(lines):
    """
    >>> part1(load_example(__file__, "25"))
    '2=-1=0'
    """
    return decimal_to_snafu(sum(snafu_to_decimal(line.strip()) for line in lines))


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2022, "25")
    print(part1(data))
