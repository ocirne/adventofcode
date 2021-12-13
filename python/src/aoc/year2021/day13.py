from aoc.util import load_input, load_example


def read_instructions(lines):
    paper = {}
    folds = []
    it = iter(lines)
    while True:
        line = next(it, None)
        if not line.strip():
            break
        x, y = map(int, line.split(","))
        paper[x, y] = True
    while True:
        line = next(it, None)
        if line is None:
            break
        axis, edge = line.split()[-1].split("=")
        folds.append((axis, int(edge)))
    return paper, folds


def fold_paper(paper, folds, just_one=False):
    for axis, edge in folds:
        tmp = {}
        for x, y in paper:
            if axis == "y" and y > edge:
                tmp[x, 2 * edge - y] = True
            elif axis == "x" and x > edge:
                tmp[2 * edge - x, y] = True
            else:
                tmp[x, y] = True
        paper = tmp
        if just_one:
            break
    return paper


def part1(lines):
    """
    >>> part1(load_example(__file__, "13"))
    17
    """
    paper, folds = read_instructions(lines)
    folded_paper = fold_paper(paper, folds, just_one=True)
    return len(folded_paper)


def part2(lines):
    paper, folds = read_instructions(lines)
    folded_paper = fold_paper(paper, folds)
    display = ""
    for y in range(6):
        for x in range(39):
            if (x, y) in folded_paper:
                display += "#"
            else:
                display += "."
        display += "\n"
    return display


if __name__ == "__main__":
    data = load_input(__file__, 2021, "13")
    print(part1(data))
    print(part2(data))
