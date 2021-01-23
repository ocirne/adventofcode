
from collections import Counter

FORBIDDEN = 'ab cd pq xy'.split()


def contains_at_least_three_vowels(s):
    c = Counter(s)
    return sum(c[x] for x in 'aeiou') >= 3


def contains_a_double_letter(s):
    for index in range(1, len(s)):
        if s[index-1] == s[index]:
            return True
    return False


def contains_no_forbidden_string(s):
    for f in FORBIDDEN:
        if f in s:
            return False
    return True


def is_nice_part1(s):
    """
    >>> is_nice_part1('ugknbfddgicrmopn')
    True
    >>> is_nice_part1('aaa')
    True
    >>> is_nice_part1('jchzalrnumimnmhp')
    False
    >>> is_nice_part1('haegwjzuvuyypxyu')
    False
    >>> is_nice_part1('dvszwmarrgswjxmb')
    False
    """
    return contains_at_least_three_vowels(s) and contains_a_double_letter(s) and contains_no_forbidden_string(s)


def contains_a_double_pair(s):
    if len(s) < 2:
        return False
    head, rest = s[:2], s[2:]
    if head in rest:
        return True
    return contains_a_double_pair(s[1:])


def contains_one_letter_between(s):
    for index in range(2, len(s)):
        if s[index-2] == s[index]:
            return True
    return False


def is_nice_part2(s):
    """
    >>> is_nice_part2('qjhvhtzxzqqjkmpb')
    True
    >>> is_nice_part2('xxyxx')
    True
    >>> is_nice_part2('aaa')
    False
    >>> is_nice_part2('uurcxstgmygtbstg')
    False
    >>> is_nice_part2('ieodomkazucvgmuy')
    False
    """
    return contains_a_double_pair(s) and contains_one_letter_between(s)


def sum_and_fun(data, fun):
    return sum(fun(line) for line in data)


if __name__ == '__main__':
    inputData = open('input', 'r').readlines()
    print(sum_and_fun(inputData, is_nice_part1))
    print(sum_and_fun(inputData, is_nice_part2))
