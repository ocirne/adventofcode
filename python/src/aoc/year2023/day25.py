from collections import defaultdict, Counter
import random

from aoc.util import load_input, load_example


class Snowverload:
    def __init__(self, lines):
        self.graph = self.read_graph(lines)
        self.result = None

    @staticmethod
    def read_graph(lines):
        graph = defaultdict(list)
        for line in lines:
            node, neighbors = line.split(": ")
            for neighbor in neighbors.split():
                graph[node].append(neighbor)
                graph[neighbor].append(node)
        return graph

    def random_node(self):
        return random.choice(list(self.graph.keys()))

    @staticmethod
    def collect_path(parent, end):
        path_node = end
        path = []
        while path_node in parent:
            next_node = parent[path_node]
            path.append((min(path_node, next_node), max(path_node, next_node)))
            path_node = next_node
        return path

    def find_random_path(self, candidates):
        start = self.random_node()
        end = self.random_node()
        open_set = [start]
        visited = set()
        parent = {}
        while open_set:
            current_node = open_set.pop(0)
            if current_node == end:
                return self.collect_path(parent, end)
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor_node in self.graph[current_node]:
                if neighbor_node in visited:
                    continue
                if (current_node, neighbor_node) in candidates:
                    continue
                if (neighbor_node, current_node) in candidates:
                    continue
                parent[neighbor_node] = current_node
                open_set.append(neighbor_node)
        # no path from start to end possible
        half = len(visited)
        if half < len(self.graph):
            self.result = (len(self.graph) - half) * half
        return None

    def divide_graph(self):
        counter = Counter()
        candidates = []
        while True:
            path_edges = self.find_random_path(candidates)
            if path_edges is None:
                return
            counter.update(path_edges)
            candidates = [p for p, _ in counter.most_common()[:3]]


def part1(lines):
    """
    >>> part1(load_example(__file__, "25"))
    54
    """
    snowverload = Snowverload(lines)
    snowverload.divide_graph()
    return snowverload.result


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2023, "25")
    print(part1(data))
