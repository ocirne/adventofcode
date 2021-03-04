from dataclasses import dataclass

from aoc.util import load_input, load_example


@dataclass
class Directions:
    dx: int
    dy: int
    ef: str
    et: str
    left: str
    lx: int
    ly: int
    right: str
    rx: int
    ry: int


D = {
    "S": Directions(0, +1, "|", "-", "E", +1, +1, "W", -1, +1),
    "N": Directions(0, -1, "|", "-", "W", -1, -1, "E", +1, -1),
    "E": Directions(+1, 0, "-", "|", "N", +1, -1, "S", +1, +1),
    "W": Directions(-1, 0, "-", "|", "S", -1, +1, "N", -1, -1),
}


class Labyrinth:
    def __init__(self, grid):
        self.grid = grid

    def find_start(self):
        line0 = self.grid[0]
        for x in range(len(line0)):
            if not line0[x].isspace():
                return x
        raise

    def f(self, x, y):
        if not 0 <= y < len(self.grid):
            return None
        if not 0 <= x < len(self.grid[y]):
            return None
        return self.grid[y][x]

    def can_go(self, x, y, e):
        field = self.f(x, y)
        if field is None:
            return False
        return field == e or field.isalpha()

    def walk(self):
        x = self.find_start()
        y = 0
        direction = "S"
        word = ""
        steps = 0
        while True:
            steps += 1
            d = D[direction]
            next_field = self.f(x + d.dx, y + d.dy)
            if next_field.isspace():
                return word, steps
            if next_field == "+":
                if self.can_go(x + 2 * d.dx, y + 2 * d.dy, d.ef):
                    pass
                elif self.can_go(x + d.lx, y + d.ly, d.et):
                    direction = d.left
                elif self.can_go(x + d.rx, y + d.ry, d.et):
                    direction = d.right
            if next_field.isalpha():
                word += next_field
            x += d.dx
            y += d.dy


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    'ABCDEF'
    """
    labyrinth = Labyrinth(lines)
    return labyrinth.walk()[0]


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    38
    """
    labyrinth = Labyrinth(lines)
    return labyrinth.walk()[1]


if __name__ == "__main__":
    data = load_input(__file__, 2017, "19")
    print(part1(data))
    print(part2(data))
