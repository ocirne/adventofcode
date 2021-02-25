from pathlib import Path
from itertools import combinations
from math import prod
from sys import maxsize


def read_data(filename):
    f = open(filename)
    return [int(line) for line in f.readlines()]


def get_minimum_quantum_entanglement(filename, compartments):
    """
    >>> part1(Path(__file__).parent / 'reference')
    99
    """
    values = read_data(filename)
    target = sum(values) // compartments
    for pick in range(1, len(values) // compartments + 1):
        quantum_entanglement = maxsize
        for c in combinations(values, pick):
            if sum(c) == target:
                quantum_entanglement = min(quantum_entanglement, prod(c))
        if quantum_entanglement < maxsize:
            return quantum_entanglement


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    99
    """
    return get_minimum_quantum_entanglement(filename, 3)


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    44
    """
    return get_minimum_quantum_entanglement(filename, 4)


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
