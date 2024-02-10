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
    def __init__(self):
        self.energy = 0
        self.spot = {}

    def readBurrow(self, lines):
        ...

    def isTarget(self):
        if self.spot.get((2, 1), None) != "A":
            return False
        if self.spot.get((2, 2), None) != "A":
            return False
        if self.spot.get((4, 1), None) != "B":
            return False
        if self.spot.get((4, 2), None) != "B":
            return False
        if self.spot.get((6, 1), None) != "C":
            return False
        if self.spot.get((6, 2), None) != "C":
            return False
        if self.spot.get((8, 1), None) != "D":
            return False
        if self.spot.get((8, 2), None) != "D":
            return False
        return True

    def move(self, amphipod, src, dst):
        assert self.spot[src] == amphipod
        assert dst not in self.spot
        #        print(amphipod, 'moves', src, '->', dst)
        sx, sy = src
        dx, dy = dst
        energy_delta = ENERGY[amphipod] * (abs(sx - dx) + abs(sy - dy))
        b = Burrow()
        b.energy = self.energy + energy_delta
        for k, v in self.spot.items():
            if k != src:
                #                print('+ k', k, 'v', v, 'src', src, 'dst', dst)
                b.spot[k] = v
            else:
                #                print('- k', k, 'v', v, 'src', src, 'dst', dst)
                ...
        b.spot[dst] = amphipod
        #        print(self.spot)
        #        print(b.spot)
        assert len(b.spot) == 8
        return b

    def hallway_spots(self, start, stop):
        if start > stop:
            start, stop = stop, start
        for h in range(start + 1, stop):
            yield h, 0

    def valid_moves(self):  # noqa: C901
        # side room -> hallway
        for side_room_x in TARGET_A.keys():
            if (side_room_x, 1) in self.spot:
                amphipod = self.spot[side_room_x, 1]
                if amphipod == TARGET_A[side_room_x] and (side_room_x, 2) and self.spot[side_room_x, 2] == amphipod:
                    continue
                for h_x in HALLWAY_X:
                    if any(s in self.spot for s in self.hallway_spots(side_room_x, h_x)):
                        continue
                    if (h_x, 0) not in self.spot:
                        yield self.move(amphipod, (side_room_x, 1), (h_x, 0))
            elif (side_room_x, 2) in self.spot:
                amphipod = self.spot[side_room_x, 2]
                if amphipod == TARGET_A[side_room_x]:
                    continue
                if (side_room_x, 1) in self.spot:
                    continue
                for h_x in HALLWAY_X:
                    if any(s in self.spot for s in self.hallway_spots(side_room_x, h_x)):
                        continue
                    if (h_x, 0) not in self.spot:
                        yield self.move(amphipod, (side_room_x, 2), (h_x, 0))
        # hallway -> side room
        for h_x in HALLWAY_X:
            if (h_x, 0) in self.spot:
                amphipod = self.spot[h_x, 0]
                side_room_x = TARGET_X[amphipod]
                # hallway muss frei sein
                if any(s in self.spot for s in self.hallway_spots(h_x, side_room_x)):
                    continue
                # oben muss immer frei sein
                elif (side_room_x, 1) in self.spot:
                    continue
                elif (side_room_x, 2) not in self.spot:
                    # unten muss frei sein
                    yield self.move(amphipod, (h_x, 0), (side_room_x, 2))
                elif self.spot[side_room_x, 2] == amphipod:
                    # oben, wenn unten bereits der richtige ist
                    yield self.move(amphipod, (h_x, 0), (side_room_x, 1))

    def __lt__(self, other):
        return True

    def str_hash(self):
        return str(sorted(self.spot.items()))


def a_star(start_burrow):
    open_heap = []
    closed_set = set()
    heappush(open_heap, (0, start_burrow))
    while open_heap:
        current_burrow = heappop(open_heap)[1]
        print("heap", len(open_heap), "energy", current_burrow.energy)
        if current_burrow.isTarget():
            return current_burrow.energy
        closed_set.add(current_burrow.str_hash())
        if len(open_heap) > 3000000:
            return -1
        if current_burrow.energy > 13_000:
            return -2
        for neighbor in current_burrow.valid_moves():
            if neighbor.str_hash() in closed_set:
                continue
            heappush(open_heap, (neighbor.energy, neighbor))


def part1(lines):
    """
    >>> part1(load_example(__file__, "23"))
    11
    """
    burrow = Burrow()
    burrow.spot[2, 1] = "B"
    burrow.spot[2, 2] = "A"
    burrow.spot[4, 1] = "C"
    burrow.spot[4, 2] = "D"
    burrow.spot[6, 1] = "B"
    burrow.spot[6, 2] = "C"
    burrow.spot[8, 1] = "D"
    burrow.spot[8, 2] = "A"

    return a_star(burrow)


def part2(lines):
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2016, "23")
    print(part1(data), "?")
    print(12521, "!")
#    print(part2(data))
