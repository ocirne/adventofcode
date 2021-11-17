from collections import Counter
from operator import itemgetter

from aoc.util import load_input
import re

ROOM_PATTERN = r"([-\w]+)-(\d+)\[(\w+)\]"
BASE = ord("a")


def deconstruct(room):
    match = re.match(ROOM_PATTERN, room)
    name = match[1]
    sector_id = int(match[2])
    checksum = match[3]
    return name, sector_id, checksum


def is_real_room(name, checksum):
    """
    >>> is_real_room('aaaaa-bbb-z-y-x', 'abxyz')
    True
    >>> is_real_room('a-b-c-d-e-f-g-h', 'abcde')
    True
    >>> is_real_room('not-a-real-room', 'oarel')
    True
    >>> is_real_room('totally-real-room', 'decoy')
    False
    """
    value = "".join(
        c for c, _ in sorted(sorted(Counter(name.replace("-", "")).items()), key=itemgetter(1), reverse=True)[:5]
    )
    return value == checksum


def sector_id_if_real_room(room):
    """
    >>> sector_id_if_real_room('aaaaa-bbb-z-y-x-123[abxyz]')
    123
    >>> sector_id_if_real_room('a-b-c-d-e-f-g-h-987[abcde]')
    987
    >>> sector_id_if_real_room('not-a-real-room-404[oarel]')
    404
    >>> sector_id_if_real_room('totally-real-room-200[decoy]')
    0
    """
    name, sector_id, checksum = deconstruct(room)
    return sector_id if is_real_room(name, checksum) else 0


def part1(lines):
    """
    >>> part1(['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]',\
               'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]'])
    1514
    """
    return sum(sector_id_if_real_room(room) for room in lines)


def rotate_char(char, sector_id):
    """
    >>> rotate_char('a', 0)
    'a'
    >>> rotate_char('a', 1)
    'b'
    >>> rotate_char('a', 25)
    'z'
    >>> rotate_char('a', 26)
    'a'
    >>> rotate_char('a', 52)
    'a'
    """
    if char == "-":
        return " "
    i = ord(char) - BASE
    d = (i + sector_id) % 26
    return chr(d + BASE)


def decrypt_room(name, sector_id):
    """
    >>> decrypt_room('qzmt-zixmtkozy-ivhz', 343)
    'very encrypted name'
    """
    return "".join(rotate_char(c, sector_id) for c in name)


def part2(lines):
    for room in lines:
        name, sector_id, _ = deconstruct(room)
        d = decrypt_room(name, sector_id)
        if "north" in d:
            return sector_id


if __name__ == "__main__":
    data = load_input(__file__, 2016, "4")
    print(part1(data))
    print(part2(data))
