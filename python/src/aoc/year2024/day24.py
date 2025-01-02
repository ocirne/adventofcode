import operator

from aoc.util import load_input, load_example


class Gate:

    def __init__(self, a, b, f, d):
        self.a = a
        self.b = b
        #        self.c = c
        self.f = f
        self.d = d


class Foo:

    def __init__(self, lines):
        self.gates = self.read_gates(lines)
        self.initial_registers = self.read_registers(lines)

    def read_gates(self, lines):
        gates = iter(lines)
        while next(gates):
            ...
        result = {}
        for line in gates:
            a, op, b, _, c = line.split(" ")
            if op == "AND":
                f, d = operator.and_, "and"
            elif op == "OR":
                f, d = operator.or_, "or"
            elif op == "XOR":
                f, d = operator.xor, "xor"
            else:
                raise
            result[c] = Gate(a, b, f, d)
        return result

    def read_registers(self, lines):
        registers = {}
        for line in lines:
            if not line:
                return registers
            key, value = line.split(": ")
            registers[key] = int(value)

    def run_simulation(self, registers):
        while any(c not in registers for c in self.gates):
            for c, gate in self.gates.items():
                if c not in registers and gate.a in registers and gate.b in registers:
                    registers[c] = gate.f(registers[gate.a], registers[gate.b])

    def collect_result(self, registers):
        result = 0
        for key in sorted((key for key in registers.keys() if key.startswith("z")), reverse=True):
            result <<= 1
            result |= registers[key]
        return result

    def foo(self, registers):
        self.run_simulation(registers)
        return self.collect_result(registers)


def part1(lines):
    """
    >>> part1(load_example(__file__, "24"))
    4
    >>> part1(load_example(__file__, "24b"))
    2024
    """
    foo = Foo(lines)
    return foo.foo(foo.initial_registers.copy())


def part2(lines):
    # wnf, vtj

    foo = Foo(lines)
    foo.gates["wnf"], foo.gates["vtj"] = foo.gates["vtj"], foo.gates["wnf"]
    foo.gates["frn"], foo.gates["z05"] = foo.gates["z05"], foo.gates["frn"]
    foo.gates["gmq"], foo.gates["z21"] = foo.gates["z21"], foo.gates["gmq"]
    foo.gates["wtt"], foo.gates["z39"] = foo.gates["z39"], foo.gates["wtt"]

    for index in range(45):
        registers = {}
        for key in foo.initial_registers:
            registers[key] = 0
        registers["x%02d" % index] = 1
        registers["y%02d" % index] = 1
        expect = 1 << (index + 1)
        actual = foo.foo(registers)
        if expect != actual:
            print("index", index, "expect", expect, "actual", actual)


#    print("digraph foo {")
#    for gate in foo.gates:
#        t = '"%s %s %s"' % (gate.a, gate.d, gate.b)
#        print(gate.a, '->', t)
#        print(gate.b, '->', t)
#        print(t, '->', gate.c)
#    print("}")

if __name__ == "__main__":
    data = load_input(__file__, 2024, "24")
    # data = load_example(__file__, "24")
    #    print(part1(data))
    print(part2(data))
