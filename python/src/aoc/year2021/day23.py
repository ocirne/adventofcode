from heapq import heappush, heappop

from aoc.util import load_input, load_example


ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}

TARGET_A = {
    2: "A",
    4: "B",
    6: "C",
    8: "D",
}

TARGET_X = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

HALLWAY_X = [0, 1, 3, 5, 7, 9, 10]


class Burrow:
    def __init__(self, depth):
        self.depth = depth
        self.energy = 0
        self.spot = {}

    def is_target(self):
        for y in range(1, self.depth + 1):
            if self.spot.get((2, y), None) != "A":
                return False
            if self.spot.get((4, y), None) != "B":
                return False
            if self.spot.get((6, y), None) != "C":
                return False
            if self.spot.get((8, y), None) != "D":
                return False
        return True

    def move(self, amphipod, src, dst):
        sx, sy = src
        dx, dy = dst
        energy_delta = ENERGY[amphipod] * (abs(sx - dx) + abs(sy - dy))
        b = Burrow(self.depth)
        b.energy = self.energy + energy_delta
        for k, v in self.spot.items():
            if k != src:
                b.spot[k] = v
        b.spot[dst] = amphipod
        return b

    def hallway_is_free(self, start, stop):
        if start > stop:
            start, stop = stop, start
        return all((h, 0) not in self.spot for h in range(start + 1, stop))

    def valid_moves(self):
        # side room -> hallway
        for side_room_x in TARGET_A.keys():
            for side_room_y in range(1, self.depth + 1):
                if (side_room_x, side_room_y) in self.spot:
                    amphipod = self.spot[side_room_x, side_room_y]
                    if all(
                        self.spot[side_room_x, y] == TARGET_A[side_room_x] for y in range(side_room_y, self.depth + 1)
                    ):
                        break
                    for h_x in HALLWAY_X:
                        if not self.hallway_is_free(side_room_x, h_x):
                            continue
                        if (h_x, 0) not in self.spot:
                            yield self.move(amphipod, (side_room_x, side_room_y), (h_x, 0))
                    break
        # hallway -> side room
        for h_x in HALLWAY_X:
            if (h_x, 0) in self.spot:
                amphipod = self.spot[h_x, 0]
                side_room_x = TARGET_X[amphipod]
                # hallway must be free
                if not self.hallway_is_free(h_x, side_room_x):
                    continue
                for side_room_y in range(self.depth, 0, -1):
                    if (side_room_x, side_room_y) in self.spot:
                        if self.spot[side_room_x, side_room_y] != amphipod:
                            break
                    else:
                        yield self.move(amphipod, (h_x, 0), (side_room_x, side_room_y))
                        break

    def __lt__(self, other):
        return self.energy < other.energy

    def str_hash(self):
        return str(sorted(self.spot.items()))


def dijkstra(start_burrow):
    open_heap = []
    closed_set = set()
    heappush(open_heap, start_burrow)
    while open_heap:
        current_burrow = heappop(open_heap)
        if current_burrow.str_hash() in closed_set:
            continue
        if current_burrow.is_target():
            return current_burrow.energy
        closed_set.add(current_burrow.str_hash())
        for neighbor in current_burrow.valid_moves():
            if neighbor.str_hash() in closed_set:
                continue
            heappush(open_heap, neighbor)


def read_burrow(lines, part2=False):
    burrow = Burrow(4 if part2 else 2)
    for y, line in enumerate(lines, start=-1):
        for x, c in enumerate(line, start=-1):
            if c.isalpha():
                burrow.spot[x, 4 if part2 and y == 2 else y] = c
    return burrow


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    12521
    """
    burrow = read_burrow(lines)
    return dijkstra(burrow)


def part2(lines):
    """
    >>> part2(load_example(__file__, "23"))
    44169
    """
    burrow = read_burrow(lines, part2=True)

    burrow.spot[2, 2] = "D"
    burrow.spot[4, 2] = "C"
    burrow.spot[6, 2] = "B"
    burrow.spot[8, 2] = "A"

    burrow.spot[2, 3] = "D"
    burrow.spot[4, 3] = "B"
    burrow.spot[6, 3] = "A"
    burrow.spot[8, 3] = "C"

    return dijkstra(burrow)


if __name__ == "__main__":
    data = load_input(__file__, 2021, "23")
    print(part1(data))
    print(part2(data))
