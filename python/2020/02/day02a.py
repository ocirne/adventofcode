
from collections import Counter


def run(filename):
    data = open(filename, 'r').readlines()
    total_valid = 0
    for line in data:
        range, letterw, password = line.split()
        min, max = map(int, range.split('-'))
        letter = letterw.split(':')[0]
        counter = Counter(password)
        count_letter = int(counter[letter])
        if min <= count_letter <= max:
            total_valid += 1
    return total_valid


assert run('reference') == 2

print(run('input'))
