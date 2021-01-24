
def prepare_data_part1(input):
    values = list(map(int, input))
    result = {values[len(values)-1]: values[0]}
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    return result


def dec(t, m):
    if t == 1:
        return m
    return t - 1


def collect_answer_part1(d):
    result = ''
    i = 1
    while d[i] != 1:
        result += str(d[i])
        i = d[i]
    return result


def read_data(filename):
    file = open(filename, 'r')
    return file.readline().strip()


def part1(data, rounds):
    """
    >>> part1('389125467', 10)
    '92658374'
    >>> part1('389125467', 100)
    '67384529'
    """
    d = prepare_data_part1(data)
    current = int(data[0])
    for _ in range(rounds):
        # pick three
        one = d[current]
        second = d[one]
        third = d[second]
        fourth = d[third]
        fifth = d[fourth]
        # nächstkleinere Zahl identifizieren
        t = dec(current, 9)
        while t in [one, second, third]:
            t = dec(t, 9)
        # umsortieren
        d[current], d[t], d[third] = fourth, one, d[t]
        # current weiterschieben
        current = d[current]
    answer = collect_answer_part1(d)
    return answer


def prepare_data_part2(input):
    m = 10**6
    values = list(map(int, input))
    result = list(range(m+1))
    for i in range(1, len(values)):
        result[values[i-1]] = values[i]
    result[values[len(values)-1]] = 10
    for i in range(11, m+1):
        result[i-1] = i
    result[m] = values[0]
    return result


def part2(data, rounds):
    """
    >>> part2('389125467', 10**7)
    149245887792
    """
    d = prepare_data_part2(data)
    current = int(data[0])
    for it in range(rounds):
        one = d[current]
        second = d[one]
        third = d[second]
        fourth = d[third]
        # nächstkleinere Zahl identifizieren
        t = dec(current, 10**6)
        while t in [one, second, third]:
            t = dec(t, 10**6)
        # umsortieren
        d[current], d[t], d[third] = fourth, one, d[t]
        # current weiterschieben
        current = d[current]
    return d[1] * d[d[1]]


if __name__ == '__main__':
    inputData = open('input', 'r').readline().strip()
    print(part1(inputData, 100))
    print(part2(inputData, 10**7))
