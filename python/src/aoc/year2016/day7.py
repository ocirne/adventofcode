from aoc.util import load_input


def separate_nets(ip, extract_valid):
    inner = []
    outer = []
    tokens = ip.split("[")
    outer.extend(extract_valid(tokens[0]))
    for t in tokens[1:]:
        left, right = t.split("]")
        inner.extend(extract_valid(left, True))
        outer.extend(extract_valid(right))
    return inner, outer


def extract_abba(word, flip=None):
    result = []
    for i in range(len(word) - 3):
        c = word[i : i + 4]
        if c[0] == c[3] and c[1] == c[2] and c[0] != c[1]:
            result.append(c)
    return result


def is_valid1(ip):
    """
    >>> is_valid1('abba[mnop]qrst')
    True
    >>> is_valid1('abcd[bddb]xyyx')
    False
    >>> is_valid1('aaaa[qwer]tyui')
    False
    >>> is_valid1('ioxxoj[asdfgh]zxcvbn')
    True
    """
    inner, outer = separate_nets(ip, extract_abba)
    return len(outer) > 0 and len(inner) == 0


def extract_aba(word, flip=False):
    result = []
    for i in range(len(word) - 2):
        c = word[i : i + 3]
        if c[0] == c[2] and c[0] != c[1]:
            if flip:
                result.append(c[1] + c[0] + c[1])
            else:
                result.append(c)
    return result


def is_valid2(ip):
    """
    >>> is_valid2('aba[bab]xyz')
    True
    >>> is_valid2('xyx[xyx]xyx')
    False
    >>> is_valid2('aaa[kek]eke')
    True
    >>> is_valid2('zazbz[bzb]cdb')
    True
    """
    inner, outer = separate_nets(ip, extract_aba)
    return bool(set(inner).intersection(set(outer)))


def count(lines, fun):
    return sum(fun(line) for line in lines)


def part1(lines):
    return count(lines, is_valid1)


def part2(lines):
    return count(lines, is_valid2)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "7")
    print(part1(data))
    print(part2(data))
