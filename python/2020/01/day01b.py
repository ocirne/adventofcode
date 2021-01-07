
M = 2020


def run(data):
    d = [int(s) for s in data]
    p = {}
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            key = d[i] + d[j]
            if key < M:
                p[key] = d[i] * d[j]
    for x in d:
        y = M - x
        if y in p:
            return x * p[y]


def data(filename):
    path = '../../../../adventofcode-input/' + filename
    file = open(path, 'r')
    return file.readlines()


assert run(data('2020/01/reference')) == 241861950

print(run(data('2020/01/input')))
