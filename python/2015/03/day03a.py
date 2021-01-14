
def run(line):
    x, y = 0, 0
    houses = {(0, 0): True}
    for d in line:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y -= 1
        elif d == 'v':
            y += 1
        else:
            raise
        houses[(x, y)] = True
    return len(houses)


assert run('>') == 2
assert run('^>v<') == 4
assert run('^v^v^v^v^v') == 2

data = open('input', 'r').readline()
print(run(data))
