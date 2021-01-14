
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


def is_nice(s):
    return contains_a_double_pair(s) and contains_one_letter_between(s)


def run(filename):
    f = open(filename, 'r')
    return sum(is_nice(line) for line in f.readlines())


assert is_nice('qjhvhtzxzqqjkmpb')
assert is_nice('xxyxx')
assert not is_nice('aaa')
assert not is_nice('uurcxstgmygtbstg')
assert not is_nice('ieodomkazucvgmuy')


print(run('input'))
