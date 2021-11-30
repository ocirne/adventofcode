from aoc.util import load_input
import regex

INVALID_PATTERN = r"\[\w*(\w)(\w)\2\1\w*\]"
VALID_PATTERN = r"(\w)(\w)\2\1"


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
    if regex.findall(INVALID_PATTERN, ip):
        return False
    m = regex.findall(VALID_PATTERN, ip)
    if not m:
        return False
    for x, y in m:
        if x != y:
            return True
    return False


def valid_triplets(word, flip=False):
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
    inner = []
    outer = []
    tokens = ip.split("[")
    outer.extend(valid_triplets(tokens[0]))
    for t in tokens[1:]:
        left, right = t.split("]")
        inner.extend(valid_triplets(left, True))
        outer.extend(valid_triplets(right))
    return bool(set(inner).intersection(set(outer)))


def count(lines, fun):
    return sum(fun(line.strip()) for line in lines)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "7")
    print(count(data, is_valid1))
    print(count(data, is_valid2))
