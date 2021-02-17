from collections import defaultdict
from typing import Callable
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Instruction:
    register: str
    change: int
    condition_register: str
    condition: Callable[[int], bool]


def create_change(direction, value):
    if direction == 'inc':
        return value
    if direction == 'dec':
        return -value
    raise


def create_condition(op, value):
    if op == '!=':
        return lambda r: r != value
    if op == '<':
        return lambda r: r < value
    if op == '<=':
        return lambda r: r <= value
    if op == '==':
        return lambda r: r == value
    if op == '>':
        return lambda r: r > value
    if op == '>=':
        return lambda r: r >= value
    raise


def create_instruction(line):
    register, direction, value, _, condition_register, op, condition_value = line.split()
    change = create_change(direction, int(value))
    condition = create_condition(op, int(condition_value))
    return Instruction(register, change, condition_register, condition)


def read_instructions(filename):
    f = open(filename, 'r')
    return [create_instruction(line) for line in f.readlines()]


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference')
    1
    """
    instructions = read_instructions(filename)
    register_bank = defaultdict(lambda: 0)
    for ins in instructions:
        if ins.condition(register_bank[ins.condition_register]):
            register_bank[ins.register] += ins.change
    return max(register_bank.values())


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    10
    """
    instructions = read_instructions(filename)
    register_bank = defaultdict(lambda: 0)
    register_max = 0
    for ins in instructions:
        if ins.condition(register_bank[ins.condition_register]):
            register_bank[ins.register] += ins.change
        register_max = max(register_max, max(register_bank.values()))
    return register_max


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
