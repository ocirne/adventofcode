from abc import ABC, abstractmethod
from collections import defaultdict
from queue import Queue

from aoc.util import load_input, load_example


class Song(ABC):
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
        return self.program[self.pc][0]

    def values(self):
        return (t for t in self.program[self.pc][1:])

    @abstractmethod
    def snd(self):
        pass

    @abstractmethod
    def rcv(self):
        pass

    def step(self):
        op = self.instruction()
        if op == "snd":
            self.snd()
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
            r = self.rcv()
            if r:
                return r
        elif op == "jgz":
            x, y = self.values()
            if self.value(x) > 0:
                self.pc += self.value(y) - 1
        else:
            raise
        self.pc += 1


class Solo(Song):
    def __init__(self, program):
        super(Solo, self).__init__(program)
        self.sound = None

    def snd(self):
        (x,) = self.values()
        self.sound = self.value(x)

    def rcv(self):
        (x,) = self.values()
        if self.value(x) != 0:
            return self.sound


class Duet(Song):
    def __init__(self, program, pid):
        super(Duet, self).__init__(program)
        self.register["p"] = pid
        self.msg_queue: Queue = Queue()
        self.other = None
        self.counter = 0

    def snd(self):
        (x,) = self.values()
        self.counter += 1
        self.other.msg_queue.put(self.value(x))

    def rcv(self):
        (x,) = self.values()
        if self.msg_queue.empty():
            return True
        else:
            self.register[x] = self.msg_queue.get()


def part1(lines):
    """
    >>> part1(load_example(__file__, "18"))
    4
    """
    program = [line.split() for line in lines]
    solo = Solo(program)
    while True:
        sound = solo.step()
        if sound:
            return sound


def part2(lines):
    program = [line.split() for line in lines]
    duet0 = Duet(program, 0)
    duet1 = Duet(program, 1)
    duet0.other = duet1
    duet1.other = duet0
    while True:
        waiting0 = duet0.step()
        waiting1 = duet1.step()
        if waiting0 and waiting1:
            break
    return duet1.counter


if __name__ == "__main__":
    data = load_input(__file__, 2017, "18")
    print(part1(data))
    print(part2(data))
