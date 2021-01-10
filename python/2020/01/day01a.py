
M = 2020


def run(filename):
    data = open(filename, 'r').readlines()
    d = {int(s) for s in data}
    for x in d:
        y = M - x
        if y in d:
            return x * y


assert run('reference') == 514579

print(run('input'))
