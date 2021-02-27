import re
from aoc.util import example


def format_bin(x):
    return '{0:36b}'.format(x)


def part1(lines):
    """
    >>> part1(example(__file__, '14a'))
    165
    """
    and_mask = or_mask = None
    d = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[2]
            and_mask = int(mask.replace('X', '1'), 2)
            or_mask = int(mask.replace('X', '0'), 2)
        else:
            _, address, _, _, str_value = re.split(r'[\[\] ]', line)
            value = int(str_value)
            d[address] = (value & and_mask) | or_mask
    return sum(d.values())


def apply_mask(mask, address):
    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += 'X'
        else:
            if address[i] == ' ':
                x = 0
            else:
                x = int(address[i])
            result += str(int(mask[i]) | x)
    return result


def floating_masks(rest, acc=''):
    if not rest:
        yield acc
    else:
        head = rest[0]
        if head == 'X':
            for x in floating_masks(rest[1:], acc + '0'):
                yield x
            for x in floating_masks(rest[1:], acc + '1'):
                yield x
        else:
            for x in floating_masks(rest[1:], acc + head):
                yield x


def part2(lines):
    """
    >>> part2(example(__file__, '14b'))
    208
    """
    mask = None
    d = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[2].strip()
        else:
            _, address, _, _, str_value = re.split(r'[\[\] ]', line)
            value = int(str_value)
            floating_mask = apply_mask(mask, format_bin(int(address)))
            for fm in floating_masks(floating_mask):
                d[fm] = value

    return sum(d.values())
