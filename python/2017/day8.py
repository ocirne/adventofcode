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


def prepare_instructions(lines):
    return [create_instruction(line) for line in lines]


def part1(lines):
    """
    >>> part1(open(Path(__file__).parent / 'examples/8.txt'))
    1
    """
    instructions = prepare_instructions(lines)
    register_bank = defaultdict(lambda: 0)
    for ins in instructions:
        if ins.condition(register_bank[ins.condition_register]):
            register_bank[ins.register] += ins.change
    return max(register_bank.values())


def part2(lines):
    """
    >>> part2(open(Path(__file__).parent / 'examples/8.txt'))
    10
    """
    instructions = prepare_instructions(lines)
    register_bank = defaultdict(lambda: 0)
    register_max = 0
    for ins in instructions:
        if ins.condition(register_bank[ins.condition_register]):
            register_bank[ins.register] += ins.change
        register_max = max(register_max, max(register_bank.values()))
    return register_max
