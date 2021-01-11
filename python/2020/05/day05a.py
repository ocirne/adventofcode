
def toInt(line):
    binRepr = line \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('R', '1') \
        .replace('L', '0')
    return int(binRepr, 2)


def run(filename):
    f = open(filename, 'r')
    lines = map(str.strip, f.readlines())
    return max(toInt(line) for line in lines)


assert run('reference') == 820

print(run('input'))
