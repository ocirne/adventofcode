from aoc.util import load_input, load_example


class Foo:
    def __init__(self, program):
        self.program = program
        self.cycle = 0
        self.x = 1
        self.baz = []

    def click(self):
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            self.baz.append(self.cycle * self.x)

    def run(self):
        for line in (s.strip() for s in self.program):
            if line == "noop":
                self.click()
            elif line.startswith("addx"):
                n = int(line.split()[1])
                self.click()
                self.click()
                self.x += n
            else:
                raise

    def bar(self):
        return self.baz


def part1(lines):
    """
    >>> part1(load_example(__file__, "10"))
    13140
    """
    foo = Foo(lines)
    foo.run()
    return sum(foo.bar())


def part2(lines):
    """
    >>> part2(load_example(__file__, "10"))
    .
    """


if __name__ == "__main__":
    data = load_input(__file__, 2022, "10")
    print(part1(data))
    print(part2(data))
