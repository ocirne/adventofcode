from aoc.util import load_input, load_example
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Score(Enum):
    WIN = 6
    DRAW = 3
    LOST = 0


# opponent, me, score
result = [
    (Shape.ROCK, Shape.ROCK, Score.DRAW),
    (Shape.ROCK, Shape.PAPER, Score.WIN),
    (Shape.ROCK, Shape.SCISSOR, Score.LOST),
    (Shape.PAPER, Shape.ROCK, Score.LOST),
    (Shape.PAPER, Shape.PAPER, Score.DRAW),
    (Shape.PAPER, Shape.SCISSOR, Score.WIN),
    (Shape.SCISSOR, Shape.ROCK, Score.WIN),
    (Shape.SCISSOR, Shape.PAPER, Score.LOST),
    (Shape.SCISSOR, Shape.SCISSOR, Score.DRAW),
]

mappingOpponent = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSOR,
}

mapping1 = {
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSOR,
}

mapping2 = {
    "X": Score.LOST,
    "Y": Score.DRAW,
    "Z": Score.WIN,
}


def scoring_part1(o, me):
    m: Shape = mapping1[me]
    s: Score = next(filter(lambda t: t[0] == o and t[1] == m, result))[2]
    return m, s


def scoring_part2(o, me):
    s: Score = mapping2[me]
    m: Shape = next(filter(lambda t: t[0] == o and t[2] == s, result))[1]
    return m, s


def score_lines(lines, fun):
    for line in lines:
        if not line:
            continue
        opponent, me = line.split()
        m, r = fun(mappingOpponent[opponent], me)
        yield m.value + r.value


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    15
    """
    return sum(score_lines(lines, scoring_part1))


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    12
    """
    return sum(score_lines(lines, scoring_part2))


if __name__ == "__main__":
    data = load_input(__file__, 2022, "2")
    print(part1(data))
    print(part2(data))
