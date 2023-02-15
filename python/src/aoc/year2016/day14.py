import hashlib
from collections import defaultdict

from aoc.util import load_input

REP = {5 * hex(i)[2:]: 3 * hex(i)[2:] for i in range(16)}


def find_three(md5_hash):
    lowest_index = 100
    result = None
    for three in REP.values():
        f = md5_hash.find(three)
        if f >= 0:
            if lowest_index > f:
                result = three
                lowest_index = f
    if lowest_index == 100:
        return None
    return result


def key_stretch(orig_hash):
    md = orig_hash
    for _ in range(2016):
        md = hashlib.md5(md.encode()).hexdigest()
    return md


def find_otp(salt, key_stretching=False):
    three_findings = defaultdict(list)
    otp_keys = set()
    i = 0
    while len(otp_keys) < 64:
        md5_hash = hashlib.md5((salt + str(i)).encode()).hexdigest()
        if key_stretching:
            md5_hash = key_stretch(md5_hash)
        three = find_three(md5_hash)
        if three is not None:
            three_findings[three].append(i)
        for f, t in REP.items():
            if f in md5_hash:
                for c in three_findings[t]:
                    if 0 < i - c < 1001:
                        otp_keys.add(c)
        i += 1
    return sorted(otp_keys)[63]


def part1(lines):
    """
    >>> part1(['abc'])
    22728
    """
    salt = lines[0]
    return find_otp(salt)


def part2(lines):
    """
    >>> part2(['abc'])
    22551
    """
    salt = lines[0]
    return find_otp(salt, key_stretching=True)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "14")
    print(part1(data))
    print(part2(data))
