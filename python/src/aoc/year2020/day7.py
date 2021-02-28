from aoc.util import load_example, load_input

from collections import defaultdict

SG = 'shiny gold'


def part1(lines):
    """
    >>> part1(load_example(__file__, '7a'))
    4
    """
    parent_colors = defaultdict(list)
    for line in lines:
        trim_line = line.strip()
        outer, inner_list = trim_line.split(' bags contain ')
        if inner_list == 'no other bags.':
            continue
        for inner in inner_list.split(','):
            _, shade, color, _ = inner.split()
            parent_colors["%s %s" % (shade, color)].append(outer)

    visited = {SG: True}
    result = [SG]
    changes = True
    while changes:
        for color in result:
            changes = False
            for parent_color in parent_colors[color]:
                if parent_color in visited:
                    continue
                changes = True
                result.append(parent_color)
                visited[parent_color] = True
    return len(result) - 1


def count_color_tree(color_tree, color):
    return 1 + sum(count * count_color_tree(color_tree, childColor) for count, childColor in color_tree[color])


def part2(lines):
    """
    >>> part2(load_example(__file__, '7b'))
    126
    """
    parent_colors = defaultdict(list)
    for line in lines:
        trim_line = line.strip()
        outer, inner_list = trim_line.split(' bags contain ')
        if inner_list == 'no other bags.':
            parent_colors[outer] = []
            continue
        for inner in inner_list.split(','):
            count, shade, color, _ = inner.split()
            parent_colors[outer].append((int(count), "%s %s" % (shade, color)))

    return count_color_tree(parent_colors, SG) - 1


if __name__ == "__main__":
    data = load_input(__file__, 2020, '6')
    print(part1(data))
    print(part2(data))
