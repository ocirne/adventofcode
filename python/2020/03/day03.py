
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




if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

def countTrees(lines, right, down):
    X = len(lines[0])
    count = 0
    x = 0
    y = 0
    while y < len(lines):
        g = lines[y][x % X]
        if g == '#':
            count += 1
        x += right
        y += down
    return count


def run(filename):
    f = open(filename, 'r')
    lines = list(map(str.strip, f.readlines()))
    a = countTrees(lines, 1, 1)
    b = countTrees(lines, 3, 1)
    c = countTrees(lines, 5, 1)
    d = countTrees(lines, 7, 1)
    e = countTrees(lines, 1, 2)
    return a*b*c*d*e


assert run('reference') == 336

print(run('input'))
