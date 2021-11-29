from aoc.util import load_input
import regex

INVALID_PATTERN = r"\.*\[\w*(\w)(\w)\2\1\w*\]\.*"
VALID_PATTERN = r"\.*(\w)(\w)\2\1\.*"


def is_valid(ip):
    """
    >>> is_valid('abba[mnop]qrst')
    True
    >>> is_valid('abcd[bddb]xyyx')
    False
    >>> is_valid('aaaa[qwer]tyui')
    False
    >>> is_valid('ioxxoj[asdfgh]zxcvbn')
    True
    """
    if regex.findall(INVALID_PATTERN, ip):
        return False
    m = regex.findall(VALID_PATTERN, ip)
    if not m:
        return False
    for x, y in m:
        if x != y:
            return True
    return False


def part1(lines):
    return sum(is_valid(line.strip()) for line in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "7")
    print(part1(data))
#    print(part2(data))
