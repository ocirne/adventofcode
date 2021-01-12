
def calc_wrapping_paper(line):
    h, l, w = sorted(map(int, line.split('x')))
    return 3*h*l + 2*h*w + 2*l*w


def run(filename):
    f = open(filename, 'r')
    return sum(calc_wrapping_paper(line) for line in f.readlines())


assert run('reference') == 101

print(run('input'))
