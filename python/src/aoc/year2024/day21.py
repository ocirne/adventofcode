from functools import lru_cache

from aoc.util import load_input, load_example

from itertools import permutations

positionsNumericKeypad = {
    '1' : (0, 2),
    '2' : (1, 2),
    '3' : (2, 2),
    '4' : (0, 1),
    '5' : (1, 1),
    '6' : (2, 1),
    '7' : (0, 0),
    '8' : (1, 0),
    '9' : (2, 0),
    '0' : (1, 3),
    'A' : (2, 3),
}

positionsDirectionalKeypad = {
    '^' : (1, 0),
    'A' : (2, 0),
    '<' : (0, 1),
    'v' : (1, 1),
    '>' : (2, 1),
}

NSWE = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

def allowedNumerical(pSrc, pTgt, move):
    px, py = pSrc
    for m in move:
        dx, dy = NSWE[m]
        px += dx
        py += dy
        if (px, py) not in positionsNumericKeypad.values():
            return False
    if (px, py) != pTgt:
        raise
    return True

## Konkrete Angebote, um von src nach tgt zu kommen
def numericKeyboard(srcChar, tgtChar):
    pSrc = positionsNumericKeypad[srcChar]
    pTgt = positionsNumericKeypad[tgtChar]
    dx = pTgt[0] - pSrc[0]
    dy = pTgt[1] - pSrc[1]
#    print(srcChar, pSrc, tgtChar, pTgt, dx, dy)
    moves = []
    if dx < 0:
        moves.extend(-dx * ['<'])
    elif dx > 0:
        moves.extend(dx * ['>'])
    if dy < 0:
        moves.extend(-dy * ['^'])
    elif dy > 0:
        moves.extend(dy * ['v'])
#    print("n moves",  moves)
    angebote = set(permutations(moves))
#    print("angebote", angebote)
    return (a for a in angebote if allowedNumerical(pSrc, pTgt, a))


def allowedDirectional(pSrc, pTgt, move):
    px, py = pSrc
    for m in move:
        dx, dy = NSWE[m]
        px += dx
        py += dy
        if (px, py) not in positionsDirectionalKeypad.values():
            return False
    if (px, py) != pTgt:
        raise
    return True

## Anzahl der Moves, um von src nach tgt zu kommen */
def directionalKeyboard(srcChar, tgtChar):
    pSrc = positionsDirectionalKeypad[srcChar]
    pTgt = positionsDirectionalKeypad[tgtChar]
    dx = pTgt[0] - pSrc[0]
    dy = pTgt[1] - pSrc[1]
    moves = []
    if dx < 0:
        moves.extend(-dx * ['<'])
    elif dx > 0:
        moves.extend(dx * ['>'])
    if dy < 0:
        moves.extend(-dy * ['^'])
    elif dy > 0:
        moves.extend(dy * ['v'])
 #   print("d moves", moves)
    return (a for a in set(permutations(moves)) if allowedDirectional(pSrc, pTgt, a))


@lru_cache(maxsize=None)
def bestDirectional(depth, s, t):
    bestSize = 10000000000000000000000000000
    for angebot in directionalKeyboard(s, t):
        if depth == 0:
            nextLevelSize = len(angebot) + 1
        else:
            nextLevelSize = countMovesDirectional1(depth-1, ['A'] + list(angebot) + ['A'])
        if bestSize > nextLevelSize:
            bestSize = nextLevelSize
    return bestSize


def countMovesDirectional1(depth, foo):
    result = 0
    for s, t in zip(foo, foo[1:]):
        result += bestDirectional(depth, s, t)
    return result

@lru_cache(maxsize=None)
def bestNumerical(depth, s, t):
    bestSize = 100000000000000000000000000000
    for angebot in numericKeyboard(s, t):
        nextLevelSize = countMovesDirectional1(depth-1, ['A'] + list(angebot) + ['A'])
        if bestSize > nextLevelSize:
            bestSize = nextLevelSize
    return bestSize

def countMovesNumeric(depth, foo):
    result = 0
    for s, t in zip(foo, foo[1:]):
        result += bestNumerical(depth, s, t)
    return result


def foo(s):
    result = countMovesNumeric(2, ['A'] + s)
    print(''.join(result))
    return len(result)



def part1(lines):
    """
    >>> part1(load_example(__file__, "21"))
    126384
    """
    total = 0
    for line in lines:
        length = foo(list(line))
        value = int(line[:-1])
        print("line", line, "length", length, "value", value)
        total += length * value
    return total


def part2(lines):
    total = 0
    for line in lines:
        length = countMovesNumeric(25, ['A'] + list(line))
        value = int(line[:-1])
        print("line", line, "length", length, "value", value)
        total += length * value
    return total

if __name__ == "__main__":
    data = load_input(__file__, 2024, "21")
    #data = load_example(__file__, "21")
    #print(part1(data))
    print(part2(data))
    print('1757129124022 (too low)')