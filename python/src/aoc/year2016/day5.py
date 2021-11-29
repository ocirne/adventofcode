import hashlib
from itertools import islice

from aoc.util import load_input


def search(door_id, is_part1=False, is_part2=False):
    i = 0
    while True:
        md5_hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if md5_hash.startswith("00000"):
            if is_part1:
                yield md5_hash[5]
            if is_part2:
                pos, char = md5_hash[5:7]
                if pos.isnumeric() and 0 <= int(pos) <= 7:
                    yield int(pos), md5_hash[6]
        i += 1


def part1(lines):
    """
    >>> part1(['abc'])
    '18f47a30'
    """
    door_id = lines[0].strip()
    return "".join(islice(search(door_id, is_part1=True), 8))


def part2(lines, be_extra_proud=True):
    """
    >>> part2(['abc'], False)
    '05ace8e3'
    """
    result = 8 * [" "]
    count = 0
    for position, character in search(lines[0].strip(), is_part2=True):
        if result[position] == " ":
            result[position] = character
            count += 1
            if count == 8:
                return "".join(result)
            if be_extra_proud:
                print("".join(result))


if __name__ == "__main__":
    data = load_input(__file__, 2016, "5")
    print(part1(data))
    print(part2(data))
