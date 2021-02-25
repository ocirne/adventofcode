import operator
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


SIGN = {'inc': 1, 'dec': -1}

OPERATORS = {
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '>': operator.gt,
    '>=': operator.ge,
}


def create_instruction(line):
    register, direction, value, _, condition_register, op, condition_value = line.split()
    change = SIGN[direction] * int(value)
    return Instruction(register, change, condition_register, lambda r: OPERATORS[op](r, int(condition_value)))


def read_instructions(filename):
    f = open(filename)
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
