
from collections import Counter


def part1(data):
    c = Counter(data)
    return c['('] - c[')']


assert run('(())') == 0
assert run('()()') == 0
assert run('(((') == 3
assert run('(()(()(') == 3
assert run('))(((((') == 3
assert run('())') == -1
assert run('))(') == -1
assert run(')))') == -3
assert run(')())())') == -3

data = open('input', 'r').readline()
print(part1(data))






def part2(data):
    floor = 0
    for index, b in enumerate(data):
        if b == '(':
            floor += 1
        elif b == ')':
            floor -= 1
        else:
            raise Exception
        if floor < 0:
            return index + 1


assert run(')') == 1
assert run('()())') == 5

data = open('input', 'r').readline()
print(run(data))







if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
