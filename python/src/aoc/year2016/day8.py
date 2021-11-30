from aoc.util import load_input
import doctest
import re

ON = "#"
OFF = "."


class Screen:
    """
    >>> doctest.ELLIPSIS_MARKER = 'dot dot dot'
    >>> example = Screen(7, 3)
    >>> example.cmd('rect 3x2')
    ###....
    ###....
    .......
    >>> example.cmd('rotate column x=1 by 1')
    #.#....
    ###....
    .#.....
    >>> example.cmd('rotate row y=0 by 4')
    dot dot dot.#.#
    ###....
    .#.....
    >>> example.cmd('rotate column x=1 by 1')
    .#..#.#
    #.#....
    .#.....
    >>> example.count()
    6
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [[OFF for _ in range(width)] for _ in range(height)]

    def _handle_rect(self, line):
        m = re.match(r"rect (\d*)x(\d*)", line)
        if m is not None:
            w, h = map(int, m.groups())
            for x in range(w):
                for y in range(h):
                    self.screen[y][x] = ON

    def _handle_rotate_row(self, line):
        m = re.match(r"rotate row y=(\d*) by (\d*)", line)
        if m is not None:
            y, count = map(int, m.groups())
            tmp = [self.screen[y][x] for x in range(self.width)]
            for x in range(self.width):
                self.screen[y][(x + count) % self.width] = tmp[x]

    def _handle_rotate_column(self, line):
        m = re.match(r"rotate column x=(\d*) by (\d*)", line)
        if m is not None:
            x, count = map(int, m.groups())
            tmp = [self.screen[y][x] for y in range(self.height)]
            for y in range(self.height):
                self.screen[(y + count) % self.height][x] = tmp[y]

    def cmd(self, line, visual=True):
        self._handle_rect(line)
        self._handle_rotate_row(line)
        self._handle_rotate_column(line)
        if visual:
            self.print()

    def print(self):
        for row in self.screen:
            print("".join(row))

    def count(self):
        return sum(sum(pixel == ON for pixel in row) for row in self.screen)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "8")
    screen = Screen(50, 6)
    for line in data:
        screen.cmd(line.strip(), visual=False)
    # part 1
    print(screen.count())
    # part 2
    screen.print()
