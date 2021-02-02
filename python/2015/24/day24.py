from pathlib import Path
from itertools import combinations
from math import prod
from sys import maxsize


def read_data(filename):
    f = open(filename, 'r')
    return [int(line) for line in f.readlines()]


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    99
    """
    values = read_data(filename)
    target = sum(values) // 3
    for pick in range(1, len(values) // 3):
        quantum_entanglement = maxsize
        for c in combinations(values, pick):
            if sum(c) == target:
                quantum_entanglement = min(quantum_entanglement, prod(c))
        if quantum_entanglement < maxsize:
            return quantum_entanglement


if __name__ == '__main__':
    print(part1('input'))
