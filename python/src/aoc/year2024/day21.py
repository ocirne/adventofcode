from aoc.util import load_input, load_example

from collections import namedtuple
from functools import lru_cache
from itertools import permutations

Position = namedtuple("Position", ["x", "y"])
Direction = namedtuple("Direction", ["dx", "dy"])


positions_numeric_keypad = {
    "1": Position(0, 2),
    "2": Position(1, 2),
    "3": Position(2, 2),
    "4": Position(0, 1),
    "5": Position(1, 1),
    "6": Position(2, 1),
    "7": Position(0, 0),
    "8": Position(1, 0),
    "9": Position(2, 0),
    "0": Position(1, 3),
    "A": Position(2, 3),
}

positions_directional_keypad = {
    "^": Position(1, 0),
    "A": Position(2, 0),
    "<": Position(0, 1),
    "v": Position(1, 1),
    ">": Position(2, 1),
}

NSWE = {
    "<": Direction(-1, 0),
    ">": Direction(1, 0),
    "^": Direction(0, -1),
    "v": Direction(0, 1),
}


def allowed(keypad, p_src, move):
    px, py = p_src
    for m in move:
        px += NSWE[m].dx
        py += NSWE[m].dy
        if (px, py) not in keypad.values():
            return False
    return True


def moves_on_keypad(keypad, src_char, tgt_char):
    p_src = keypad[src_char]
    p_tgt = keypad[tgt_char]
    dx = p_tgt.x - p_src.x
    dy = p_tgt.y - p_src.y
    moves = []
    if dx < 0:
        moves.extend(-dx * ["<"])
    elif dx > 0:
        moves.extend(dx * [">"])
    if dy < 0:
        moves.extend(-dy * ["^"])
    elif dy > 0:
        moves.extend(dy * ["v"])
    return ("".join(a) for a in set(permutations(moves)) if allowed(keypad, p_src, a))


def count_moves_keypad(depth, keypad_sequence, f):
    return sum(f(depth, s, t) for s, t in zip(keypad_sequence, keypad_sequence[1:]))


@lru_cache(maxsize=None)
def best_directional(depth, s, t):
    if depth == 0:
        return len(next(moves_on_keypad(positions_directional_keypad, s, t))) + 1
    return min(
        count_moves_keypad(depth - 1, "A" + angebot + "A", best_directional)
        for angebot in moves_on_keypad(positions_directional_keypad, s, t)
    )


def best_numerical(depth, s, t):
    return min(
        count_moves_keypad(depth - 1, "A" + angebot + "A", best_directional)
        for angebot in moves_on_keypad(positions_numeric_keypad, s, t)
    )


def shortest_button_sequence(line, depth):
    length = count_moves_keypad(depth, "A" + line, best_numerical)
    value = int(line[:-1])
    return length * value


def sum_all_button_sequences(lines, depth):
    return sum(shortest_button_sequence(line, depth) for line in lines)


def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    126384
    """
    return sum_all_button_sequences(lines, 2)


def part2(lines):
    return sum_all_button_sequences(lines, 25)


if __name__ == "__main__":
    data = load_input(__file__, 2024, "21")
    print(part1(data))
    print(part2(data))
