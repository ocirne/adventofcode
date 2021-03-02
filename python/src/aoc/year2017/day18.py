from collections import defaultdict
from queue import Queue

from aoc.util import load_input, load_example


class Solo:
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
    return Solo(program).execute()


class Duet:
    def __init__(self, program, pid):
        self.program = program
        self.register = defaultdict(lambda: 0)
        self.pid = pid
        self.register["p"] = pid
        self.pc = 0
        self.msg_queue: Queue = Queue()
        self.other = None
        self.counter = 0

    def value(self, t):
        if t.isalpha():
            return self.register[t]
        else:
            return int(t)

    def instruction(self):
        return self.program[self.pc][0]

    def values(self):
        return (t for t in self.program[self.pc][1:])

    def execute_instruction(self):
        waiting = None
        op = self.instruction()
        if op == "snd":
            (x,) = self.values()
            self.counter += 1
            self.other.msg_queue.put(self.value(x))
        elif op == "set":
            x, y = self.values()
            self.register[x] = self.value(y)
        elif op == "add":
            x, y = self.values()
            self.register[x] += self.value(y)
        elif op == "mul":
            x, y = self.values()
            self.register[x] *= self.value(y)
        elif op == "mod":
            x, y = self.values()
            self.register[x] %= self.value(y)
        elif op == "rcv":
            (x,) = self.values()
            if self.msg_queue.empty():
                self.pc -= 1
                waiting = True
            else:
                self.register[x] = self.msg_queue.get()
        elif op == "jgz":
            x, y = self.values()
            if self.value(x) > 0:
                self.pc += self.value(y) - 1
        else:
            raise
        self.pc += 1
        return waiting


def part2(lines):
    program = [line.strip().split() for line in lines]
    duet0 = Duet(program, 0)
    duet1 = Duet(program, 1)
    duet0.other = duet1
    duet1.other = duet0
    while True:
        wait0 = duet0.execute_instruction()
        wait1 = duet1.execute_instruction()
        if wait0 and wait1:
            break
    return duet1.counter


if __name__ == "__main__":
    data = load_input(__file__, 2017, "18")
    print(part1(data))
    print(part2(data))
