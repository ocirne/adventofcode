from aoc.util import load_input, load_example


M = {
    ">": (+1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, +1),
}

CD = {
    "/>": "^",
    "/<": "v",
    "/^": ">",
    "/v": "<",
    "\\>": "v",
    "\\<": "^",
    "\\^": "<",
    "\\v": ">",
    "|>": "^v",
    "|<": "^v",
    "-^": "<>",
    "-v": "<>",
}


class CaveBeam:
    def __init__(self, w, h, lines):
        self.w, self.h = w, h
        self.cave = self.read_cave(lines)

    @staticmethod
    def read_cave(lines):
        cave = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                cave[x, y] = c
        return cave

    def neighbors(self, px, py, d):
        for nd in CD.get(self.cave[px, py] + d, d):
            dx, dy = M[nd]
            yield px + dx, py + dy, nd

    def dijkstra(self, px, py, d):
        open_set = {(px, py, d)}
        visited = {}
        while open_set:
            px, py, d = open_set.pop()
            visited[px, py] = d
            for nx, ny, nd in self.neighbors(px, py, d):
                if not (0 <= nx < self.w and 0 <= ny < self.h):
                    continue
                if (nx, ny) in visited and visited[nx, ny] == nd:
                    continue
                open_set.add((nx, ny, nd))
        return len(visited)


def part1(lines):
    """
    >>> part1(load_example(__file__, "16"))
    46
    """
    w, h = len(lines[0]), len(lines)
    return CaveBeam(w, h, lines).dijkstra(0, 0, ">")


def try_all_beams(lines):
    w, h = len(lines[0]), len(lines)
    for sx in range(w):
        yield CaveBeam(w, h, lines).dijkstra(sx, 0, "v")
        yield CaveBeam(w, h, lines).dijkstra(sx, h - 1, "^")
    for sy in range(h):
        yield CaveBeam(w, h, lines).dijkstra(0, sy, ">")
        yield CaveBeam(w, h, lines).dijkstra(w - 1, sy, "<")


def part2(lines):
    """
    >>> part2(load_example(__file__, "16"))
    51
    """
    return max(try_all_beams(lines))


if __name__ == "__main__":
    data = load_input(__file__, 2023, "16")
    print(part1(data))
    print(part2(data))
