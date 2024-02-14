from abc import ABC, abstractmethod

from aoc.util import load_input, load_example
import re

RDLU = {
    0: (+1, 0),  # right
    1: (0, +1),  # down
    2: (-1, 0),  # left
    3: (0, -1),  # up
}

"""
          (2,0)
(0,1)(1,1)(2,1)
          (2,2)(3,2)
"""

dice_jumps_3d_test = {
    ((0, 1), 0): ((1, 1), 0, lambda s, x, y: (0, y)),
    ((0, 1), 1): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((0, 1), 2): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((0, 1), 3): ((2, 0), 1, lambda s, x, y: (s - x, 0)),
    ((1, 1), 0): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((1, 1), 1): ((2, 2), 0, lambda s, x, y: (0, x)),
    ((1, 1), 2): ((0, 1), 2, lambda s, x, y: (s, y)),
    ((1, 1), 3): ((2, 0), 0, lambda s, x, y: (0, x)),
    ((2, 0), 0): ((3, 2), 2, lambda s, x, y: (s, y)),
    ((2, 0), 1): ((2, 1), 1, lambda s, x, y: (x, s - y)),
    ((2, 0), 2): ((1, 1), 1, lambda s, x, y: (y, 0)),
    ((2, 0), 3): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((2, 1), 0): ((3, 2), 1, lambda s, x, y: (s - y, 0)),
    ((2, 1), 1): ((2, 2), 1, lambda s, x, y: (x, 0)),
    ((2, 1), 2): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((2, 1), 3): ((2, 0), 3, lambda s, x, y: (x, s)),
    ((2, 2), 0): ((3, 2), 0, lambda s, x, y: (0, y)),
    ((2, 2), 1): ((0, 1), 3, lambda s, x, y: (s - x, s)),
    ((2, 2), 2): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((2, 2), 3): ((2, 1), 3, lambda s, x, y: (x, s)),
    ((3, 2), 0): ((7, 7), 7, lambda s, x, y: (x, y)),
    ((3, 2), 1): ((2, 0), 2, lambda s, x, y: (s, s - y)),
    ((3, 2), 2): ((2, 2), 2, lambda s, x, y: (s, y)),
    ((3, 2), 3): ((7, 7), 7, lambda s, x, y: (x, y)),
}


"""
     (1,0)(2,0)
     (1,1)
(0,2)(1,2)
(0,3)
"""

dice_jumps_3d = {
    ((0, 2), 0): ((1, 2), 0, lambda s, x, y: (0, y)),
    ((0, 2), 1): ((0, 3), 1, lambda s, x, y: (x, 0)),
    ((0, 2), 2): ((1, 0), 0, lambda s, x, y: (0, s - y)),
    ((0, 2), 3): ((1, 1), 0, lambda s, x, y: (0, x)),
    ((0, 3), 0): ((1, 2), 3, lambda s, x, y: (y, s)),
    ((0, 3), 1): ((2, 0), 1, lambda s, x, y: (x, 0)),
    ((0, 3), 2): ((1, 0), 1, lambda s, x, y: (y, 0)),
    ((0, 3), 3): ((0, 2), 3, lambda s, x, y: (x, s)),
    ((1, 0), 0): ((2, 0), 0, lambda s, x, y: (0, y)),
    ((1, 0), 1): ((1, 1), 1, lambda s, x, y: (x, 0)),
    ((1, 0), 2): ((0, 2), 0, lambda s, x, y: (0, s - y)),
    ((1, 0), 3): ((0, 3), 0, lambda s, x, y: (0, x)),
    ((1, 1), 0): ((2, 0), 3, lambda s, x, y: (y, s)),
    ((1, 1), 1): ((1, 2), 1, lambda s, x, y: (x, 0)),
    ((1, 1), 2): ((0, 2), 1, lambda s, x, y: (y, 0)),
    ((1, 1), 3): ((1, 0), 3, lambda s, x, y: (x, s)),
    ((1, 2), 0): ((2, 0), 2, lambda s, x, y: (s, s - y)),
    ((1, 2), 1): ((0, 3), 2, lambda s, x, y: (s, x)),
    ((1, 2), 2): ((0, 2), 2, lambda s, x, y: (s, y)),
    ((1, 2), 3): ((1, 1), 3, lambda s, x, y: (x, s)),
    ((2, 0), 0): ((1, 2), 2, lambda s, x, y: (s, s - y)),
    ((2, 0), 1): ((1, 1), 2, lambda s, x, y: (s, x)),
    ((2, 0), 2): ((1, 0), 2, lambda s, x, y: (s, y)),
    ((2, 0), 3): ((0, 3), 3, lambda s, x, y: (x, s)),
}


class Board(ABC):
    def __init__(self, lines, size):
        self.board = self._read_board(lines, size)
        self.path = lines[-1]
        self.size = size

    @abstractmethod
    def _read_board(self, lines, size):
        ...

    @abstractmethod
    def _neighbor(self, cq, cf, cx, cy, dx, dy):
        ...

    def follow_path(self, start_quadrant=(0, 0)):
        q, f, x, y = start_quadrant, 0, 0, 0
        for t in re.split("([RL])", self.path):
            if t.isnumeric():
                for _ in range(int(t)):
                    dx, dy = RDLU[f]
                    tmp = self._neighbor(q, f, x, y, dx, dy)
                    if tmp is None:
                        break
                    q, f, x, y = tmp
            elif t == "R":
                f = (f + 1) % 4
            elif t == "L":
                f = (f + 3) % 4
            else:
                raise
        qx, qy = q
        return 1000 * (qy * self.size + y + 1) + 4 * (qx * self.size + x + 1) + f


class Board2D(Board):
    def __init__(self, lines):
        super().__init__(lines, 0)

    def _read_board(self, lines, _):
        board = {}
        for y, line in enumerate(lines[:-2]):
            for x, c in enumerate(line):
                if not c.isspace():
                    board[x, y] = c
        return board

    def _neighbor(self, cq, cf, cx, cy, dx, dy):
        nx, ny = cx + dx, cy + dy
        if (nx, ny) not in self.board:
            if cf == 0:
                nx = min(x for x, y in self.board.keys() if y == ny)
            elif cf == 1:
                ny = min(y for x, y in self.board.keys() if x == nx)
            elif cf == 2:
                nx = max(x for x, y in self.board.keys() if y == ny)
            elif cf == 3:
                ny = max(y for x, y in self.board.keys() if x == nx)
        if self.board[nx, ny] == "#":
            return None
        return cq, cf, nx, ny


class Board3D(Board):
    def __init__(self, lines, size, dice_jumps):
        super().__init__(lines, size)
        self.dice_jumps = dice_jumps

    def _read_board(self, lines, size):
        board = {}
        for y, line in enumerate(lines[:-2]):
            for x, c in enumerate(line):
                if not c.isspace():
                    q = x // size, y // size
                    if q not in board:
                        board[q] = {}
                    board[q][x % size, y % size] = c
        return board

    def _neighbor(self, cq, cf, cx, cy, dx, dy):
        nq, nf, nx, ny = cq, cf, cx + dx, cy + dy
        if (nx, ny) not in self.board[cq]:
            nq, nf, jump_func = self.dice_jumps[cq, cf]
            nx, ny = jump_func(self.size - 1, cx, cy)
        if self.board[nq][nx, ny] == "#":
            return None
        return nq, nf, nx, ny


def part1(lines):
    """
    >>> part1(load_example(__file__, "22"))
    6032
    """
    return Board2D(lines).follow_path()


def part2(lines, size=50, dice_jumps=None, start_quadrant=(1, 0)):
    """
    >>> part2(load_example(__file__, "22"), size=4, dice_jumps=dice_jumps_3d_test, start_quadrant=(2, 0))
    5031
    """
    if dice_jumps is None:
        dice_jumps = dice_jumps_3d
    return Board3D(lines, size, dice_jumps).follow_path(start_quadrant)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "22")
    print(part1(data))
    print(part2(data))
