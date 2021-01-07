
M = 2020


def run(data):
    d = {int(s) for s in data}
    for x in d:
        y = M - x
        if y in d:
            return x * y


def data(filename):
    path = '../../../../adventofcode-input/' + filename
    file = open(path, 'r')
    return file.readlines()


assert run(data('2020/01/reference')) == 514579

print(run(data('2020/01/input')))
