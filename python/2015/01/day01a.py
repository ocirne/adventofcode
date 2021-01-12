
from collections import Counter


def run(data):
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
print(run(data))
