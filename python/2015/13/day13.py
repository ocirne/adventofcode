from collections import defaultdict
from itertools import permutations
from pathlib import Path


def read_data(filename, with_me):
    f = open(filename)
    guests = {}
    happiness = defaultdict(lambda: 0)
    for line in f.readlines():
        token = line.strip().strip('.').split()
        guest, direction, value, neighbor = [token[i] for i in [0, 2, 3, 10]]
        guests[guest] = True
        if direction == 'gain':
            happiness[(guest, neighbor)] += int(value)
            happiness[(neighbor, guest)] += int(value)
        elif direction == 'lose':
            happiness[(guest, neighbor)] -= int(value)
            happiness[(neighbor, guest)] -= int(value)
        else:
            raise
    if with_me:
        for guest in guests.keys():
            happiness[(guest, 'me')] = 0
            happiness[('me', guest)] = 0
        guests['me'] = True
    return list(guests.keys()), happiness


def calc_happiness(happiness, arrangement):
    return happiness[(arrangement[0], arrangement[-1])] +\
           sum(happiness[(arrangement[i-1], arrangement[i])] for i in range(1, len(arrangement)))


def run(filename, with_me):
    """
    >>> run(Path(__file__).parent / 'reference', False)
    330
    """
    guests, happiness = read_data(filename, with_me)
    return max(calc_happiness(happiness, arrangement) for arrangement in permutations(guests))


if __name__ == '__main__':
    print(run('input', with_me=False))
    print(run('input', with_me=True))
