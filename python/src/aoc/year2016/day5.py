import hashlib
from itertools import islice

from aoc.util import load_input


def search(door_id):
    i = 0
    while True:
        md5_hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if md5_hash.startswith("00000"):
            print(i, md5_hash, md5_hash[5])
            yield md5_hash[5]
        i += 1


def part1(lines):
    """
    >>> part1(['abc'])
    '18f47a30'
    """
    return "".join(islice(search(lines[0].strip()), 8))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "5")
    print(part1(data))
#    print(part2(data))
