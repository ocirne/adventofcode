from itertools import permutations

from aoc.util import load_input, load_example


def rotate_left(word, x):
    return word[x:] + word[:x]


def rotate_right(word, x):
    return word[-x:] + word[:-x]


def scramble(instructions, password, verbose):
    sp = password
    for instruction in instructions:
        token = instruction.split()
        if instruction.startswith("swap position"):
            x, y = int(token[2]), int(token[5])
            sp[x], sp[y] = sp[y], sp[x]
        elif instruction.startswith("swap letter"):
            x, y = token[2], token[5]
            xi = sp.index(x)
            yi = sp.index(y)
            sp[xi], sp[yi] = sp[yi], sp[xi]
        elif instruction.startswith("rotate left"):
            x = int(token[2])
            sp = rotate_left(sp, x)
        elif instruction.startswith("rotate right"):
            x = int(token[2])
            sp = rotate_right(sp, x)
        elif instruction.startswith("rotate based on position"):
            x = token[6]
            index = sp.index(x)
            sp = rotate_right(sp, 1)
            sp = rotate_right(sp, index)
            if index >= 4:
                sp = rotate_right(sp, 1)
        elif instruction.startswith("reverse positions"):
            x, y = int(token[2]), int(token[4]) + 1
            sp = sp[:x] + list(reversed(sp[x:y])) + sp[y:]
        elif instruction.startswith("move position"):
            x, y = int(token[2]), int(token[5])
            if x < y:
                sp = sp[:x] + sp[x + 1 : y + 1] + sp[x : x + 1] + sp[y + 1 :]
            else:
                sp = sp[:y] + sp[x : x + 1] + sp[y:x] + sp[x + 1 :]
        else:
            raise
        if verbose:
            print("".join(sp))
    return "".join(sp)


def part1(lines, password="abcdefgh", verbose=False):
    """
    >>> part1(load_example(__file__, "21"), password="abcde", verbose=True)
    ebcda
    edcba
    abcde
    bcdea
    bdeac
    abdec
    ecabd
    decab
    'decab'
    """
    sp = list(password)
    return scramble(lines, sp, verbose)


def part2(lines):
    for p in permutations("abcdefgh"):
        if scramble(lines, list(p), False) == "fbgdceah":
            return "".join(p)


if __name__ == "__main__":
    data = load_input(__file__, 2016, "21")
    print(part1(data))
    print(part2(data))
