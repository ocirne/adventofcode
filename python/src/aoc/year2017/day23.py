from collections import defaultdict

from aoc.util import load_input


class Coprocessor:
    def __init__(self, program):
        self.program = program
        self.register = defaultdict(lambda: 0)
        self.pc = 0

    def value(self, t):
        if t.isalpha():
            return self.register[t]
        else:
            return int(t)

    def instruction(self):
        if 0 <= self.pc < len(self.program):
            return self.program[self.pc][0]

    def values(self):
        return (t for t in self.program[self.pc][1:])

    def execute(self):
        count_mul = 0
        while True:
            op = self.instruction()
            if op is None:
                return count_mul
            elif op == "set":
                x, y = self.values()
                self.register[x] = self.value(y)
            elif op == "sub":
                x, y = self.values()
                self.register[x] -= self.value(y)
            elif op == "mul":
                count_mul += 1
                x, y = self.values()
                self.register[x] *= self.value(y)
            elif op == "jnz":
                x, y = self.values()
                if self.value(x) != 0:
                    self.pc += self.value(y) - 1
            else:
                raise
            self.pc += 1


def part1(lines):
    program = [line.strip().split() for line in lines]
    coprocessor = Coprocessor(program)
    return coprocessor.execute()


if __name__ == "__main__":
    data = load_input(__file__, 2017, "23")
    print(part1(data))
