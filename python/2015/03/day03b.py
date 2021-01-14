
def move(d, x, y):
    if d == '>':
        return x + 1, y
    elif d == '<':
        return x - 1, y
    elif d == '^':
        return x, y - 1
    elif d == 'v':
        return x, y + 1
    raise


def run(line):
    sx, sy, rx, ry = 0, 0, 0, 0
    houses = {(0, 0): True}
    for index, d in enumerate(line):
        if index % 2 == 0:
            sx, sy = move(d, sx, sy)
            houses[(sx, sy)] = True
        else:
            rx, ry = move(d, rx, ry)
            houses[(rx, ry)] = True
    return len(houses)


assert run('^v') == 3
assert run('^>v<') == 3
assert run('^v^v^v^v^v') == 11


data = open('input', 'r').readline()
print(run(data))
