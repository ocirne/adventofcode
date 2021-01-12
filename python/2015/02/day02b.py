
def calc_wrapping_paper(line):
    h, l, w = sorted(map(int, line.split('x')))
    return 2*(h+l) + h*l*w


def run(filename):
    f = open(filename, 'r')
    return sum(calc_wrapping_paper(line) for line in f.readlines())


assert run('reference') == 48

print(run('input'))
