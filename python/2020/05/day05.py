
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



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

def toInt(seatId):
    binRepr = seatId \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('R', '1') \
        .replace('L', '0')
    return int(binRepr, 2)


def run(filename):
    f = open(filename, 'r')
    lines = map(str.strip, f.readlines())
    seats = sorted(toInt(line) for line in lines)
    for i in range(1, len(seats)):
        if seats[i-1] != seats[i] - 1:
            return seats[i]-1


print(run('input'))
