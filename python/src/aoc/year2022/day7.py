from aoc.util import load_input, load_example


class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = size


def calc_sizes(node):
    if not node.children:
        return
    for child in node.children:
        calc_sizes(child)
    node.size = sum(child.size for child in node.children)


def collect_sizes(node):
    if not node.children:
        return []
    sizes = [node.size]
    for child in node.children:
        for sub_size in collect_sizes(child):
            sizes.append(sub_size)
    return sizes


def part1(lines):
    """
    >>> part1(load_example(__file__, "7"))
    95437
    """
    root: Node
    pwd: Node
    for line in lines:
        print(line)
        if line.startswith("$ cd"):
            directory = line.strip().split()[2]
            if directory == "/":
                root = Node(directory, None)
                pwd = root
            elif directory == "..":
                pwd = pwd.parent
            else:
                child = next(child for child in pwd.children if child.name == directory)
                pwd = child
        elif line.startswith("$ ls"):
            # can be ignored
            ...
        elif line.startswith("dir"):
            directory = line.strip().split()[1]
            pwd.children.append(Node(directory, pwd))
        else:
            size, name = line.strip().split()
            pwd.children.append(Node(name, pwd, int(size)))

    calc_sizes(root)
    return sum(size for size in collect_sizes(root) if size < 100_000)


def part2(lines):
    """
    >>> part2(load_example(__file__, "7"))
    .
    """


if __name__ == "__main__":
    data = load_input(__file__, 2022, "7")
    print(part1(data))
#    print(part2(data))
