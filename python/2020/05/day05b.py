
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
