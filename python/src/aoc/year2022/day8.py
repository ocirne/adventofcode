from aoc.util import load_input, load_example


class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False
        self.scenic_score = None


class Forest:
    def __init__(self, lines):
        self.trees = {}
        for y, line in enumerate(lines):
            for x, height in enumerate(line):
                self.trees[x, y] = Tree(int(height))
        self.max_xy = len(lines)

    def count_visible(self):
        return sum(1 for tree in self.trees.values() if tree.visible)

    def look_all_directions(self):
        # from north
        self.look(True, range(self.max_xy))
        # from south
        self.look(True, range(self.max_xy - 1, -1, -1))
        # from west
        self.look(False, range(self.max_xy))
        # from east
        self.look(False, range(self.max_xy - 1, -1, -1))

    def look(self, vertical, y_range):
        for x in range(self.max_xy):
            last_height = -1
            for y in y_range:
                tree = self.trees[x, y] if vertical else self.trees[y, x]
                if last_height < tree.height:
                    tree.visible = True
                    last_height = tree.height
                if tree.height == 9:
                    # shortcut, all other trees are not visible
                    break

    def calc_scenic_scores(self):
        for (x, y), tree in self.trees.items():
            n = self.calc_scenic_score(x, y, tree, 0, -1)
            s = self.calc_scenic_score(x, y, tree, 0, 1)
            e = self.calc_scenic_score(x, y, tree, 1, 0)
            w = self.calc_scenic_score(x, y, tree, -1, 0)
            tree.scenic_score = n * s * e * w

    def calc_scenic_score(self, sx, sy, base, dx, dy):
        x, y = sx, sy
        max_height = base.height
        while True:
            if not (x + dx, y + dy) in self.trees:
                break
            x += dx
            y += dy
            tree = self.trees[x, y]
            if tree.height >= max_height:
                break
        return max(abs(x - sx), abs(y - sy))

    def best_scenic_score(self):
        return max(tree.scenic_score for tree in self.trees.values())


def part1(lines):
    """
    >>> part1(load_example(__file__, "8"))
    21
    """
    forest = Forest(lines)
    forest.look_all_directions()
    return forest.count_visible()


def part2(lines):
    """
    >>> part2(load_example(__file__, "8"))
    8
    """
    forest = Forest(lines)
    forest.calc_scenic_scores()
    return forest.best_scenic_score()


if __name__ == "__main__":
    data = load_input(__file__, 2022, "8")
    print(part1(data))
    print(part2(data))
