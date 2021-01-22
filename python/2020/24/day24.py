
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



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

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

def countEnv(endpoints, x, y):
    result = 0
    if (x, y-1) in endpoints:
        result += 1
    if (x+1, y-1) in endpoints:
        result += 1
    if (x-1, y+1) in endpoints:
        result += 1
    if (x, y+1) in endpoints:
        result += 1
    if (x-1, y) in endpoints:
        result += 1
    if (x+1, y) in endpoints:
        result += 1
    return result


def simulateRound(oldEndpoints):
    result = {}
    minX = min(x for x, _ in oldEndpoints) - 1
    maxX = max(x for x, _ in oldEndpoints) + 2
    minY = min(y for _, y in oldEndpoints) - 1
    maxY = max(y for _, y in oldEndpoints) + 2
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            count = countEnv(oldEndpoints, x, y)
            if (x, y) in oldEndpoints:
                if not (count == 0 or count > 2):
                    result[(x, y)] = True
            else:
                if count == 2:
                    result[(x, y)] = True
    return result


def simulate(paraEndpoints, rounds):
    endpoints = paraEndpoints
    for _ in range(rounds):
        endpoints = simulateRound(endpoints)
    return len(endpoints)


def run(filename, rounds):
    data = readData(filename)
    endpoints = [endpoint(line) for line in data]
    realEndpoints = {ep: True for ep, count in Counter(endpoints).items() if count % 2 == 1}
    return simulate(realEndpoints, rounds)


assert run('reference', 0) == 10
assert run('reference', 1) == 15
assert run('reference', 2) == 12
assert run('reference', 3) == 25
assert run('reference', 4) == 14
assert run('reference', 5) == 23
assert run('reference', 6) == 28
assert run('reference', 7) == 41
assert run('reference', 8) == 37
assert run('reference', 9) == 49
assert run('reference', 10) == 37

assert run('reference', 20) == 132
assert run('reference', 30) == 259
assert run('reference', 40) == 406
assert run('reference', 50) == 566
assert run('reference', 60) == 788
assert run('reference', 70) == 1106
assert run('reference', 80) == 1373
assert run('reference', 90) == 1844
assert run('reference', 100) == 2208

print(run('input', 100))
