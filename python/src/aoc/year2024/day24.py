import operator

from aoc.util import load_input, load_example


class Gate:

    def __init__(self, a, b, c, f):
        self.a = a
        self.b = b
        self.c = c
        self.f = f

class Foo:

    def __init__(self, lines):
        self.gates = list(self.read_gates(lines))

    def read_gates(self, lines):
        gates = iter(lines)
        while next(gates):
            ...
        for line in gates:
            a, op, b, _, c = line.split(' ')
            if op == 'AND':
                f = operator.and_
            elif op == 'OR':
                f = operator.or_
            elif op == 'XOR':
                f = operator.xor
            else:
                raise
            yield Gate(a, b, c, f)

    def read_registers(self, lines):
        registers = {}
        for line in lines:
            if not line:
                return registers
            key, value = line.split(": ")
            registers[key] = int(value)

    def run_simulation(self):
        while any(gate.c not in self.registers for gate in self.gates):
            for gate in self.gates:
                if gate.c not in self.registers and gate.a in self.registers and gate.b in self.registers:
                    self.registers[gate.c] = gate.f(self.registers[gate.a], self.registers[gate.b])

    def collect_result(self):
        result = 0
        for key in sorted((key for key in self.registers.keys() if key.startswith("z")), reverse=True):
            result <<= 1
            result |= self.registers[key]
        return result

    def foo(self, lines):
        self.registers = self.read_registers(lines)
        self.run_simulation()
        return self.collect_result()


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    4
    >>> part1(load_example(__file__, "24b"))
    2024
    """
    foo = Foo(lines)
    return foo.foo(lines)


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2024, "24")
    # data = load_example(__file__, "24")
    print(part1(data))
#    print(part2(data))
