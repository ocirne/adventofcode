
from collections import Counter


def readData(filename):
    f = open(filename, 'r')
    return (line.strip() for line in f.readlines())


def endpoint(line, x=0, y=0):
    if line == '':
        return x, y
    if line.startswith('nw'):
        return endpoint(line[2:], x, y-1)
    if line.startswith('ne'):
        return endpoint(line[2:], x+1, y-1)
    if line.startswith('sw'):
        return endpoint(line[2:], x-1, y+1)
    if line.startswith('se'):
        return endpoint(line[2:], x, y+1)
    if line.startswith('w'):
        return endpoint(line[1:], x-1, y)
    if line.startswith('e'):
        return endpoint(line[1:], x+1, y)
    else:
        raise Exception


def run(filename):
    data = readData(filename)
    endpoints = [endpoint(line) for line in data]
    return sum(1 for v in Counter(endpoints).values() if v % 2 == 1)


assert endpoint('nwwswee') == (0, 0)
assert run('reference') == 10

print(run('input'))
