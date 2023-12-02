from aoc.util import load_input, load_example


def foo(game):
    game_rounds = game.split(": ")[1].split(";")
    for game_round in game_rounds:
        for count_name in game_round.split(","):
            count, name = count_name.split()
            if name == "red" and int(count) > 12:
                return False
            if name == "green" and int(count) > 13:
                return False
            if name == "blue" and int(count) > 14:
                return False
    return True


def part1(lines):
    """
    >>> part1(load_example(__file__, "2"))
    8
    """
    total = 0
    for id0, game in enumerate(lines):
        if foo(game):
            total += id0 + 1
    return total


def bar(game):
    red = green = blue = 0
    game_rounds = game.split(": ")[1].split(";")
    for game_round in game_rounds:
        for count_name in game_round.split(","):
            count, name = count_name.split()
            if name == "red":
                red = max(red, int(count))
            if name == "green":
                green = max(green, int(count))
            if name == "blue":
                blue = max(blue, int(count))
    return red * green * blue


def part2(lines):
    """
    >>> part2(load_example(__file__, "2"))
    2286
    """
    total = 0
    for id0, game in enumerate(lines):
        total += bar(game)
    return total


if __name__ == "__main__":
    data = load_input(__file__, 2023, "2")
    print(part1(data))
    print(part2(data))
