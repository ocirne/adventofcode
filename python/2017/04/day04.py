from collections import Counter


def is_valid_part1(line):
    """
    >>> is_valid_part1('aa bb cc dd ee')
    True
    >>> is_valid_part1('aa bb cc dd aa')
    False
    >>> is_valid_part1('aa bb cc dd aaa')
    True
    """
    return max(Counter(line.split()).values()) == 1


def is_valid_part2(line):
    """
    >>> is_valid_part2('abcde fghij')
    True
    >>> is_valid_part2('abcde xyz ecdab')
    False
    >>> is_valid_part2('a ab abc abd abf abj')
    True
    >>> is_valid_part2('iiii oiii ooii oooi oooo')
    True
    >>> is_valid_part2('oiii ioii iioi iiio')
    False
    """
    return max(Counter(''.join(sorted(word)) for word in line.split()).values()) == 1


def run(data, is_valid):
    return sum(is_valid(line.strip()) for line in data)


if __name__ == '__main__':
    inputData = open('input', 'r').readlines()
    print(run(inputData, is_valid_part1))
    print(run(inputData, is_valid_part2))
