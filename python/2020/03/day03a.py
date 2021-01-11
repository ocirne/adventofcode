
def run(filename):
    f = open(filename, 'r')
    lines = list(map(str.strip, f.readlines()))
    X = len(lines[0])
    countTrees = 0
    x = 0
    y = 0
    while y < len(lines):
        g = lines[y][x % X]
        if g == '#':
            countTrees += 1
        x += 3
        y += 1
    return countTrees


assert run('reference') == 7

print(run('input'))
