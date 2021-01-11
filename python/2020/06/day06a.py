
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
