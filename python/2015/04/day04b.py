
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
