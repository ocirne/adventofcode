
import hashlib


def check(s, zeros):
    return hashlib.md5(s.encode()).hexdigest().startswith(zeros * '0')


def search(base, zeros):
    """
    >>> search('abcdef', 5)
    609043
    >>> search('pqrstuv', 5)
    1048970
    """
    i = 0
    while True:
        if check(base + str(i), zeros):
            return i
        i += 1


if __name__ == '__main__':
    data = open('input').readline()
    print(search(data, 5))
    print(search(data, 6))
