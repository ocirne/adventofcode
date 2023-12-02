from collections import defaultdict

from aoc.util import load_input, load_example

MAXIMA_PART1 = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def iter_colors(game):
    game_rounds = game.split(": ")[1].split(";")
    for game_round in game_rounds:
        for count_color in game_round.split(","):
            count, color = count_color.split()
            yield int(count), color


def find_valid_games(game):
    return all(count <= MAXIMA_PART1[color] for count, color in iter_colors(game))


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    8
    """
    return sum(id0 + 1 for id0, game in enumerate(lines) if find_valid_games(game))


def find_minimum_count(game):
    d = defaultdict(int)
    for count, color in iter_colors(game):
        d[color] = max(d[color], count)
    return d["red"] * d["green"] * d["blue"]


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    2286
    """
    return sum(find_minimum_count(game) for id0, game in enumerate(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "2")
    print(part1(data))
    print(part2(data))
