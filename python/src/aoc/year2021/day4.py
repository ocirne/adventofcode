from aoc.util import load_input, load_example


class Board:
    def __init__(self, lines):
        self.board = [[int(n) for n in line.split()] for line in lines]
        self.marks = [[False for _ in range(5)] for _ in range(5)]

    def mark(self, number):
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == number:
                    self.marks[y][x] = True

    def wins(self):
        for i in range(5):
            if all(self.marks[i][j] for j in range(5)) or all(self.marks[j][i] for j in range(5)):
                return True
        return False

    def unmarked(self):
        for y in range(5):
            for x in range(5):
                if not self.marks[y][x]:
                    yield self.board[y][x]


def read_data(lines):
    numbers = [int(n) for n in lines[0].split(",")]
    boards = [Board(lines[ln : ln + 5]) for ln in range(2, len(lines), 6)]
    return numbers, boards


def part1(lines):
    """
    >>> part1(load_example(__file__, "4"))
    4512
    """
    numbers, boards = read_data(lines)
    for number in numbers:
        for b in boards:
            b.mark(number)
        for b in boards:
            if b.wins():
                return sum(b.unmarked()) * number


def part2(lines):
    """
    >>> part2(load_example(__file__, "4"))
    1924
    """
    numbers, boards = read_data(lines)
    for number in numbers:
        for b in boards:
            b.mark(number)
        for b in boards:
            if b.wins():
                if len(boards) == 1:
                    return sum(b.unmarked()) * number
                boards.remove(b)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "4")
    print(part1(data))
    print(part2(data))
