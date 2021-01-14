
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


def is_nice(s):
    return contains_at_least_three_vowels(s) and contains_a_double_letter(s) and contains_no_forbidden_string(s)


def run(filename):
    f = open(filename, 'r')
    return sum(is_nice(line) for line in f.readlines())


assert is_nice('ugknbfddgicrmopn')
assert is_nice('aaa')
assert not is_nice('jchzalrnumimnmhp')
assert not is_nice('haegwjzuvuyypxyu')
assert not is_nice('dvszwmarrgswjxmb')


print(run('input'))
