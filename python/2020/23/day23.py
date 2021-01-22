
def prepareData(input):
    values = list(map(int, input))
    result = {values[len(values)-1]: values[0]}
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    return result


def dec(t):
    if t == 1:
        return 9
    return t - 1


def collectAnswer(d):
    result = ''
    i = 1
    while d[i] != 1:
        result += str(d[i])
        i = d[i]
    return result


def read_data(filename):
    file = open(filename, 'r')
    return file.readline().strip()


def run(filename, rounds):
    data = read_data(filename)
    d = prepareData(data)
    current = int(data[0])
    for _ in range(rounds):
        # pick three
        one = d[current]
        second = d[one]
        third = d[second]
        fourth = d[third]
        fifth = d[fourth]
        # nächstkleinere Zahl identifizieren
        t = dec(current)
        while t in [one, second, third]:
            t = dec(t)
        # umsortieren
        d[current], d[t], d[third] = fourth, one, d[t]
        # current weiterschieben
        current = d[current]
    answer = collectAnswer(d)
    return answer


assert run('reference', 10) == '92658374'
assert run('reference', 100) == '67384529'

print(run('input', 100))




if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

M = 10**6


def prepareData(input):
    values = list(map(int, input))
    result = list(range(M+1))
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    result[values[len(values)-1]] = 10
    for i in range(11, M+1):
        result[i-1] = i
    result[M] = values[0]
    return result


def dec(t):
    if t == 1:
        return M
    return t - 1


def collectAnswer(d):
    a = d[1]
    b = d[d[1]]
    return a*b


def read_data(filename):
    file = open(filename, 'r')
    return file.readline().strip()


def run(filename, rounds):
    data = read_data(filename)
    d = prepareData(data)
    current = int(data[0])
    for it in range(rounds):
        one = d[current]
        second = d[one]
        third = d[second]
        fourth = d[third]
        # nächstkleinere Zahl identifizieren
        t = dec(current)
        while t in [one, second, third]:
            t = dec(t)
        # umsortieren
        d[current], d[t], d[third] = fourth, one, d[t]
        # current weiterschieben
        current = d[current]
    answer = collectAnswer(d)
    return answer


assert run('reference', 10**7) == 149245887792


print(run('input', 10**7))
