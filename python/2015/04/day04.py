
import hashlib


def check(s):
    return hashlib.md5(s.encode()).hexdigest().startswith(5 * '0')


def run(base):
    i = 0
    while True:
        if check(base + str(i)):
            return i
        i += 1


assert run('abcdef') == 609043
assert run('pqrstuv') == 1048970


data = open('input', 'r').readline()
print(run(data))



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

import hashlib


def check(s):
    return hashlib.md5(s.encode()).hexdigest().startswith(6 * '0')


def run(base):
    i = 0
    while True:
        if check(base + str(i)):
            return i
        i += 1


data = open('input', 'r').readline()
print(run(data))