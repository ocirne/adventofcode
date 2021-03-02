from collections import defaultdict

from aoc.util import load_input, load_example


class Duet:
    def __init__(self, program):
        self.program = program
        self.register = defaultdict(lambda: 0)

    def value(self, t):
        if t.isalpha():
            return self.register[t]
        else:
            return int(t)

    def instruction(self, pc):
        return self.program[pc][0]

    def values(self, pc):
        return (t for t in self.program[pc][1:])

    def execute(self):
        pc = 0
        sound = None
        while True:
            op = self.instruction(pc)
            if op == "snd":
                (x,) = self.values(pc)
                sound = self.value(x)
            elif op == "set":
                x, y = self.values(pc)
                self.register[x] = self.value(y)
            elif op == "add":
                x, y = self.values(pc)
                self.register[x] += self.value(y)
            elif op == "mul":
                x, y = self.values(pc)
                self.register[x] *= self.value(y)
            elif op == "mod":
                x, y = self.values(pc)
                self.register[x] %= self.value(y)
            elif op == "rcv":
                (x,) = self.values(pc)
                if self.value(x) != 0:
                    return sound
            elif op == "jgz":
                x, y = self.values(pc)
                if self.value(x) > 0:
                    pc += self.value(y) - 1
            else:
                raise
            pc += 1


def part1(lines):
    """
    >>> part1(load_example(__file__, "18"))
    4
    """
    program = [line.strip().split() for line in lines]
    return Duet(program).execute()


if __name__ == "__main__":
    data = load_input(__file__, 2017, "18")
    print(part1(data))
