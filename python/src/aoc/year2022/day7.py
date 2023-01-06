from aoc.util import load_input, load_example


class Node:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = size

    def calculate_sizes(self):
        if not self.children:
            return
        for child in self.children:
            child.calculate_sizes()
        self.size = sum(child.size for child in self.children)

    def collect_sizes(self):
        if not self.children:
            return []
        sizes = [self.size]
        for child in self.children:
            for sub_size in child.collect_sizes():
                sizes.append(sub_size)
        return sizes


def create_tree(lines):
    root = Node("/", None)
    pwd = root
    for line in lines:
        if line.startswith("$ cd"):
            directory = line.strip().split()[2]
            if directory == "/":
                # ignored, using knowledge that only first line is "$ cd /"
                ...
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
    root.calculate_sizes()
    return root


def part1(lines):
    """
    >>> part1(load_example(__file__, "7"))
    95437
    """
    root = create_tree(lines)
    return sum(size for size in root.collect_sizes() if size < 100_000)


def part2(lines):
    """
    >>> part2(load_example(__file__, "7"))
    24933642
    """
    root = create_tree(lines)
    sizes = root.collect_sizes()
    necessary = root.size - (70000000 - 30000000)
    return min(size for size in sizes if size >= necessary)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "7")
    print(part1(data))
    print(part2(data))
