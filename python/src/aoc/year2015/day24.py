from aoc.util import load_example, load_input
from itertools import combinations
from math import prod
from sys import maxsize


def get_minimum_quantum_entanglement(lines, compartments):
    """
    >>> part1(load_example(__file__, '24'))
    99
    """
    values = [int(line) for line in lines]
    target = sum(values) // compartments
    for pick in range(1, len(values) // compartments + 1):
        quantum_entanglement = maxsize
        for c in combinations(values, pick):
            if sum(c) == target:
                quantum_entanglement = min(quantum_entanglement, prod(c))
        if quantum_entanglement < maxsize:
            return quantum_entanglement


def part1(lines):
    """
    >>> part1(load_example(__file__, '24'))
    99
    """
    return get_minimum_quantum_entanglement(lines, 3)


def part2(lines):
    """
    >>> part2(load_example(__file__, '24'))
    44
    """
    return get_minimum_quantum_entanglement(lines, 4)


if __name__ == "__main__":
    data = load_input(__file__, 2015, "24")
    print(part1(data))
    print(part2(data))
