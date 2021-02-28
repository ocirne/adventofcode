from aoc.util import load_input

CA = 97
CO = ord('o') - CA
CI = ord('i') - CA
CL = ord('l') - CA


def to_int_array(s):
    """
    >>> to_int_array('abc')
    [0, 1, 2]
    >>> to_int_array('oil')
    [14, 8, 11]
    """
    return [ord(c) - CA for c in s]


def to_char_array(i):
    """
    >>> to_char_array([0, 1, 2, 25])
    'abcz'
    """
    return ''.join([chr(x + CA) for x in i])


def is_run(part):
    """
    >>> is_run([4])
    False
    >>> is_run([1, 2, 3])
    True
    >>> is_run([3, 2, 1])
    False
    """
    if len(part) != 3:
        return False
    return part[0] + 2 == part[1] + 1 == part[2]


def is_pair(part):
    """
    >>> is_pair([4])
    False
    >>> is_pair([4, 4])
    True
    >>> is_pair([6, 9])
    False
    """
    if len(part) != 2:
        return False
    return part[0] == part[1]


def inc_pos(arr, pos, force):
    changed = False
    if force:
        arr[pos] = arr[pos] + 1
        changed = True
    if arr[pos] in [CO, CI, CL]:
        arr[pos] = arr[pos] + 1
        changed = True
    if changed:
        for i in range(pos + 1, len(arr)):
            arr[i] = 0


def find_next(arr, depth=0, run=False, pair1=None, pos1=None, letter1=None, pair2=None):
    if depth == len(arr):
        return run and pair1 and pair2
    while True:
        inc_pos(arr, depth, False)
        if pair1:
            r_pair1, r_pos1, r_letter1 = True, pos1, letter1
        elif is_pair(arr[depth-1:depth+1]):
            r_pair1, r_pos1, r_letter1 = True, depth, arr[depth]
        else:
            r_pair1, r_pos1, r_letter1 = False, None, None
        r_pair2 = pair2 or (pair1 and depth > pos1 + 1 and arr[depth] != letter1 and is_pair(arr[depth-1:depth+1]))
        if find_next(arr,
                     depth + 1,
                     run or is_run(arr[depth-2:depth+1]),
                     r_pair1, r_pos1, r_letter1,
                     r_pair2):
            return True
        inc_pos(arr, depth, True)
        if arr[depth] > 25:
            return False


def inc_password(ipw):
    """
    >>> inc_password([0, 1, 2, 3, 4, 5, 6, 7])
    [0, 1, 2, 3, 4, 5, 6, 8]
    >>> inc_password([0, 0, 0, 0, 0, 0, 0, 25])
    [0, 0, 0, 0, 0, 0, 1, 0]
    >>> inc_password([0, 0, 0, 0, 5, 25, 25, 25])
    [0, 0, 0, 0, 6, 0, 0, 0]
    """
    result = ipw[:]
    i = len(result) - 1
    while True:
        result[i] += 1
        if result[i] > 25:
            result[i] = 0
            i -= 1
        else:
            return result


def next_password(spw, is_valid):
    """
    >>> next_password('abcdefgh', False)
    'abcdffaa'
    >>> next_password('ghijklmn', False)
    'ghjaabcc'
    """
    ipw = to_int_array(spw)
    if is_valid:
        ipw = inc_password(ipw)
    find_next(ipw)
    return to_char_array(ipw)


def part1(lines):
    return next_password(lines[0], False)


def part2(lines):
    answer1 = part1(lines)
    return next_password(answer1, True)


if __name__ == "__main__":
    data = load_input(__file__, 2015, '11')
    print(part1(data))
    print(part2(data))
