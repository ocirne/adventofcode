from heapq import heappush, heappop

from aoc.util import load_input, load_example

BASE = ord("a")


class HeightMap:
    def __init__(self, lines):
        self.heightmap = {}
        self.height = len(lines)
        for y, row in enumerate(line.strip() for line in lines):
            self.width = len(row)
            for x, mark in enumerate(row):
                position = x, y
                if mark == "S":
                    self.start = position
                    self.heightmap[position] = ord("a") - BASE
                elif mark == "E":
                    self.target = position
                    self.heightmap[position] = ord("z") - BASE
                else:
                    self.heightmap[position] = ord(mark) - BASE

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.heightmap[x, y], end=" ")
            print()

    def find_neighbors(self, current_node):
        cx, cy = current_node
        neighbors = []
        if cx > 0:
            neighbors.append((cx - 1, cy))
        if cx + 1 < self.width:
            neighbors.append((cx + 1, cy))
        if cy > 0:
            neighbors.append((cx, cy - 1))
        if cy + 1 < self.height:
            neighbors.append((cx, cy + 1))
        return (n for n in neighbors if self.heightmap[current_node] - self.heightmap[n] <= 1)

    def find_path(self, is_target):
        """A* from endpoint E to start (part1) or any elevation a (part2)"""
        start_node = self.target
        open_heap = []
        closed_set = set()
        parent = {}
        g = {start_node: 0}
        heappush(open_heap, (0, self.target))
        while open_heap:
            current_node = heappop(open_heap)[1]
            if is_target(current_node):
                length = 0
                while current_node in parent:
                    length += 1
                    current_node = parent[current_node]
                return length
            closed_set.add(current_node)
            # expand node
            for neighbor in self.find_neighbors(current_node):
                if neighbor in closed_set:
                    continue
                tentative_g = g[current_node] + 1
                if neighbor in closed_set and tentative_g >= g[neighbor]:
                    continue
                if tentative_g < g.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap]:
                    parent[neighbor] = current_node
                    g[neighbor] = tentative_g
                    heappush(open_heap, (tentative_g, neighbor))


def part1(lines):
    """
    >>> part1(load_example(__file__, "12"))
    31
    """
    heightmap = HeightMap(lines)
    return heightmap.find_path(lambda target: target == heightmap.start)


def part2(lines):
    """
    >>> part2(load_example(__file__, "12"))
    29
    """
    heightmap = HeightMap(lines)
    return heightmap.find_path(lambda target: heightmap.heightmap[target] == 0)


if __name__ == "__main__":
    data = load_input(__file__, 2022, "12")
    print(part1(data))
    print(part2(data))
