from aoc.util import load_input, load_example


class Foo:
    def __init__(self, program):
        self.program = program
        self.cycle = 0
        self.x = 1
        self.baz = []
        self.crt = [40 * ["."] for _ in range(6)]

    def click(self):
        self.cycle += 1
        # part1
        if (self.cycle - 20) % 40 == 0:
            self.baz.append(self.cycle * self.x)
        # part2
        pos = self.cycle - 1
        if self.x - 1 <= pos % 40 <= self.x + 1:
            self.crt[pos // 40][pos % 40] = "#"

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

    def print_crt(self):
        for line in self.crt:
            print("".join(line))


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
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    """
    foo = Foo(lines)
    foo.run()
    foo.print_crt()


if __name__ == "__main__":
    data = load_input(__file__, 2022, "10")
    print(part1(data))
    print(part2(data))
