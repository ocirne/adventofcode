from aoc.util import load_input


def find_sop_marker(message, marker):
    i = marker
    while True:
        if len(set(message[i - marker : i])) == marker:
            return i
        i += 1


def part1(lines):
    """
    >>> part1(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"])
    7
    >>> part1(["bvwbjplbgvbhsrlpgdmjqwftvncz"])
    5
    >>> part1(["nppdvjthqldpwncqszvftbrmjlhg"])
    6
    >>> part1(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"])
    10
    >>> part1(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"])
    11
    """
    return find_sop_marker(lines[0], 4)


def part2(lines):
    """
    >>> part2(["mjqjpqmgbljsphdztnvjfqwrcgsmlb"])
    19
    >>> part2(["bvwbjplbgvbhsrlpgdmjqwftvncz"])
    23
    >>> part2(["nppdvjthqldpwncqszvftbrmjlhg"])
    23
    >>> part2(["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"])
    29
    >>> part2(["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"])
    26
    """
    return find_sop_marker(lines[0], 14)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "6")
    print(part1(data))
    print(part2(data))
