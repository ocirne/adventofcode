
def run(filename):
    f = open(filename, 'r')
    answers = []
    a = {}
    for line in f.readlines():
        if not line.strip():
            answers.append(len(a.keys()))
            a = {}
        else:
            for k in line.strip():
                a[k] = True
    answers.append(len(a.keys()))
    return sum(answers)


assert run('reference') == 11

print(run('input'))



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

from collections import defaultdict


def run(filename):
    f = open(filename, 'r')
    answers = []
    a = defaultdict(lambda: 0)
    countPeople = 0
    for line in f.readlines():
        if not line.strip():
            answers.append(len([1 for v in a.values() if v == countPeople]))
            a = defaultdict(lambda: 0)
            countPeople = 0
        else:
            for k in line.strip():
                a[k] += 1
            countPeople += 1
    answers.append(len([1 for v in a.values() if v == countPeople]))
    return sum(answers)


assert run('reference') == 6

print(run('input'))
