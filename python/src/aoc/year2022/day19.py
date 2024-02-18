from collections import defaultdict
from heapq import heappush, heappop
from typing import Tuple

from aoc.util import load_input, load_example
import re

# TODO
# flake8: noqa


BLUEPRINT_PATTERN = re.compile(
    r"^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$"  # noqa: E501
)

ORE = 3  # "ore"
CLAY = 2  # "clay"
OBSIDIAN = 1  # "obsidian"
GEODE = 0  # "geode"
FINISH = 42

resource = (ORE, CLAY, OBSIDIAN, GEODE)


def collect_geodes0(line):
    m = BLUEPRINT_PATTERN.match(line)
    if not m:
        raise line
    print(line)
    (
        index,
        ore_ore_cost,
        clay_ore_cost,
        obsidian_ore_cost,
        obsidian_clay_cost,
        geode_ore_cost,
        geode_obsidian_cost,
    ) = map(int, m.groups())
    print(
        index, ore_ore_cost, clay_ore_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost
    )

    minerals = {r: 0 for r in resource}
    robots = {r: 0 for r in resource}
    robots[ORE] = 1
    for minute in range(24):
        print("=== Minute %d ===" % (minute + 1))
        new_robots = defaultdict(bool)
        # build new robots

        # geode robot wird immer gebaut
        if minerals[ORE] >= geode_ore_cost and minerals[OBSIDIAN] >= geode_obsidian_cost:
            minerals[ORE] -= geode_ore_cost
            minerals[OBSIDIAN] -= geode_obsidian_cost
            new_robots[GEODE] = True
            print(
                "Spend %d ore and %d obsidian to start building a geode-collecting robot."
                % (geode_ore_cost, geode_obsidian_cost)
            )

        # obsidian robot wird nur gebaut, wenn ore nicht für geode robot gebraucht wird
        # d.h.
        # anzahl runden bis genug obsidian da ist > anzahl runden bis genug ore da ist
        # geode_obsidian_cost / robots[OBSIDIAN] <-> obsidian_ore_cost / robots[ORE]

        if (
            minerals[ORE] >= obsidian_ore_cost
            and minerals[CLAY] >= obsidian_clay_cost
            and minerals[OBSIDIAN] < geode_obsidian_cost
        ):
            minerals[ORE] -= obsidian_ore_cost
            minerals[CLAY] -= obsidian_clay_cost
            new_robots[OBSIDIAN] = True
            print(
                "Spend %d ore and %d clay to start building a obsidian-collecting robot."
                % (obsidian_ore_cost, obsidian_clay_cost)
            )

        if minerals[ORE] >= clay_ore_cost and minerals[CLAY] < obsidian_clay_cost:
            minerals[ORE] -= clay_ore_cost
            new_robots[CLAY] = True
            print("Spend %d ore to start building a clay-collecting robot." % clay_ore_cost)

        if minerals[ORE] >= ore_ore_cost and minerals[CLAY] < obsidian_clay_cost:
            minerals[ORE] -= ore_ore_cost
            new_robots[ORE] = True
            print("Spend %d ore to start building a ore-collecting robot." % ore_ore_cost)
        # collecting
        for r in resource:
            if robots[r] > 0:
                minerals[r] += robots[r]
                print(
                    "%d %s-collecting robot collects %d %s; you now have %d %s."
                    % (robots[r], r.value, robots[r], r.value, minerals[r], r.value)
                )
        # new robots
        for r in resource:
            if new_robots[r]:
                robots[r] += 1
                print("The new %s-collecting robot is ready; you now have %d of them." % (r.value, robots[r]))
        print()

    return 1 * minerals[GEODE]


class Node:
    def __init__(self, minute, minerals, robots, forbidden):
        self.minute = minute
        self.minerals = minerals
        self.robots = robots
        self.forbidden = forbidden

    def __lt__(self, other):
        return self.minute < other.minute

    def __eq__(self, other):
        return (
            isinstance(other, Node)
            and self.minute == other.minute
            and self.minerals == other.minerals
            and self.robots == other.robots
            and str(sorted(self.forbidden)) == str(sorted(other.forbidden))
        )

    def __hash__(self):
        return hash((self.minute, self.minerals, self.robots, str(sorted(self.forbidden))))

    def __str__(self):
        return "min %s minerals %s robots %s forbidden %s" % (self.minute, self.minerals, self.robots, self.forbidden)


class Foo:
    def __init__(self, line, cut_points):
        m = BLUEPRINT_PATTERN.match(line)
        (
            self.index,
            self.ore_ore_cost,
            self.clay_ore_cost,
            self.obsidian_ore_cost,
            self.obsidian_clay_cost,
            self.geode_ore_cost,
            self.geode_obsidian_cost,
        ) = map(int, m.groups())
        self.best_can_do = -1
        self.best_node = None
        self.cut_points = cut_points
        self.best_geodes = {0: 0}

    def dfs(self, minute: int, minerals: Tuple[int, int, int, int], robots: Tuple[int, int, int, int]):
        if minute > 19 and robots[GEODE] < 1:
            return
        if minute > 22 and robots[GEODE] < 2:
            return
        if minute > 12 and robots[OBSIDIAN] < 1:
            return
        if minute > 16 and robots[OBSIDIAN] < 2:
            return
        if minute > 14 and robots[CLAY] < 4:
            return
        if minute > 15 and robots[CLAY] < 1:
            return
        if minute > 2 and robots[ORE] < 1:
            return
        if minute == 25:
            #    print('minute', minute, 'heap', 'minerals', minerals, 'robots', robots, 'best', self.best_can_do)
            #            print(', '.join("%s: %s" % (key.value, value) for key, value in minerals.items()))
            self.best_can_do = max(self.best_can_do, minerals[GEODE])
            return
        can_build_any = False
        for new_robot in (GEODE, OBSIDIAN, CLAY, ORE, None):
            # build new robot
            can_build = False
            delta_geode = 0
            delta_obsidian = 0
            delta_clay = 0
            delta_ore = 0
            if new_robot == GEODE:
                if minerals[ORE] >= self.geode_ore_cost and minerals[OBSIDIAN] >= self.geode_obsidian_cost:
                    can_build = True
                    delta_obsidian = self.geode_obsidian_cost
                    delta_ore = self.geode_ore_cost

            elif new_robot == OBSIDIAN:
                if minerals[ORE] >= self.obsidian_ore_cost and minerals[CLAY] >= self.obsidian_clay_cost:
                    can_build = True
                    delta_clay = self.obsidian_clay_cost
                    delta_ore = self.obsidian_ore_cost

            elif new_robot == CLAY:
                if minerals[ORE] >= self.clay_ore_cost:
                    can_build = True
                    delta_ore = self.clay_ore_cost

            elif new_robot == ORE:
                if minerals[ORE] >= self.ore_ore_cost:
                    can_build = True
                    delta_ore = self.ore_ore_cost

            # collecting
            minerals2 = (
                minerals[GEODE] - delta_geode + robots[GEODE],
                minerals[OBSIDIAN] - delta_obsidian + robots[OBSIDIAN],
                minerals[CLAY] - delta_clay + robots[CLAY],
                minerals[ORE] - delta_ore + robots[ORE],
            )
            if can_build:
                robots2 = (
                    robots[GEODE] + int(new_robot == GEODE),
                    robots[OBSIDIAN] + int(new_robot == OBSIDIAN),
                    robots[CLAY] + int(new_robot == CLAY),
                    robots[ORE] + int(new_robot == ORE),
                )
                self.dfs(minute + 1, minerals2, robots2)

        minerals2 = (
            minerals[GEODE] + robots[GEODE],
            minerals[OBSIDIAN] + robots[OBSIDIAN],
            minerals[CLAY] + robots[CLAY],
            minerals[ORE] + robots[ORE],
        )
        self.dfs(minute + 1, minerals2, robots)

    def collect_geodes1(self):
        minerals = (0, 0, 0, 0)
        robots = (0, 0, 0, 1)

        self.dfs(1, minerals, robots)
        #  print('best_can_do', self.best_can_do)
        return self.index * self.best_can_do

    def find_neighbors(self, node: Node):
        for cut_minute, material, minimum in self.cut_points:
            if node.minute > cut_minute and node.robots[material] < minimum:
                return
        if node.minute == 24:
            # print('minute', node.minute, 'heap', 'minerals', node.minerals, 'robots', node.robots, 'forbidden', node.forbidden, 'best', self.best_can_do)
            #            print(', '.join("%s: %s" % (key.value, value) for key, value in minerals.items()))
            if self.best_can_do < node.minerals[GEODE]:
                self.best_can_do = node.minerals[GEODE]
                self.best_node = node
            return
        # build new robot
        # Geode robot - always building, never forbidden
        if node.minerals[ORE] >= self.geode_ore_cost and node.minerals[OBSIDIAN] >= self.geode_obsidian_cost:
            minerals2 = (
                node.minerals[GEODE] + node.robots[GEODE],
                node.minerals[OBSIDIAN] - self.geode_obsidian_cost + node.robots[OBSIDIAN],
                node.minerals[CLAY] + node.robots[CLAY],
                node.minerals[ORE] - self.geode_ore_cost + node.robots[ORE],
            )
            robots2 = (node.robots[GEODE] + 1, node.robots[OBSIDIAN], node.robots[CLAY], node.robots[ORE])
            yield Node(node.minute + 1, minerals2, robots2, set())

        else:
            could_build = set()
            # obsidian robot
            if (
                OBSIDIAN not in node.forbidden
                and node.minerals[ORE] >= self.obsidian_ore_cost
                and node.minerals[CLAY] >= self.obsidian_clay_cost
            ):
                could_build.add(OBSIDIAN)
                minerals2 = (
                    node.minerals[GEODE] + node.robots[GEODE],
                    node.minerals[OBSIDIAN] + node.robots[OBSIDIAN],
                    node.minerals[CLAY] - self.obsidian_clay_cost + node.robots[CLAY],
                    node.minerals[ORE] - self.obsidian_ore_cost + node.robots[ORE],
                )
                robots2 = (node.robots[GEODE], node.robots[OBSIDIAN] + 1, node.robots[CLAY], node.robots[ORE])
                yield Node(node.minute + 1, minerals2, robots2, set())

            # clay robot
            if CLAY not in node.forbidden and node.minerals[ORE] >= self.clay_ore_cost:
                could_build.add(CLAY)
                minerals2 = (
                    node.minerals[GEODE] + node.robots[GEODE],
                    node.minerals[OBSIDIAN] + node.robots[OBSIDIAN],
                    node.minerals[CLAY] + node.robots[CLAY],
                    node.minerals[ORE] - self.clay_ore_cost + node.robots[ORE],
                )
                robots2 = (node.robots[GEODE], node.robots[OBSIDIAN], node.robots[CLAY] + 1, node.robots[ORE])
                yield Node(node.minute + 1, minerals2, robots2, set())

            # ore robot
            if ORE not in node.forbidden and node.minerals[ORE] >= self.ore_ore_cost:
                could_build.add(ORE)
                minerals2 = (
                    node.minerals[GEODE] + node.robots[GEODE],
                    node.minerals[OBSIDIAN] + node.robots[OBSIDIAN],
                    node.minerals[CLAY] + node.robots[CLAY],
                    node.minerals[ORE] - self.ore_ore_cost + node.robots[ORE],
                )
                robots2 = (node.robots[GEODE], node.robots[OBSIDIAN], node.robots[CLAY], node.robots[ORE] + 1)
                yield Node(node.minute + 1, minerals2, robots2, set())

            # no robot, forbid all robots which could be build, but didn't
            minerals2 = (
                node.minerals[GEODE] + node.robots[GEODE],
                node.minerals[OBSIDIAN] + node.robots[OBSIDIAN],
                node.minerals[CLAY] + node.robots[CLAY],
                node.minerals[ORE] + node.robots[ORE],
            )
            yield Node(node.minute + 1, minerals2, node.robots, node.forbidden.union(could_build))

    def dijkstra(self):  # , cut_point=100):
        open_heap = []
        closed_set = set()
        heappush(open_heap, Node(0, (0, 0, 0, 0), (0, 0, 0, 1), set()))
        while open_heap:
            current = heappop(open_heap)
            print(len(open_heap), current.minute)
            if current.minerals[GEODE] < self.best_geodes[current.minute]:
                continue
            if current.minute > 24:
                continue
            if current in closed_set:
                continue
            closed_set.add(current)
            for neighbor in self.find_neighbors(current):
                if neighbor in closed_set:
                    continue
                self.best_geodes[neighbor.minute] = max(
                    self.best_geodes.get(neighbor.minute, 0), neighbor.minerals[GEODE]
                )
                heappush(open_heap, neighbor)
        return self.best_can_do


def find_cut_point(line, material, cut_point):
    for minimum in range(20, 0, -1):
        cut_points = [
            (cut_point, material, minimum),
        ]
        if Foo(line, cut_points).dijkstra(cut_point + 1) == -2:
            print(material, minimum, "at", cut_point)
            return minimum


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    0 -> 9
    1 -> 12
    """
    #    print(Foo(lines[0]).collect_geodes1())

    #    find_cut_point(lines[0], GEODE, 10)
    #    find_cut_point(lines[0], OBSIDIAN, 10)
    #    find_cut_point(lines[0], CLAY, 10)
    #    find_cut_point(lines[0], ORE, 10)

    #    find_cut_point(lines[0], GEODE, 15)
    #    find_cut_point(lines[0], OBSIDIAN, 15)
    #    find_cut_point(lines[0], CLAY, 15)
    #    find_cut_point(lines[0], ORE, 15)

    cut_points = [
        #        (18, GEODE, 1),
        #        (21, GEODE, 2),
        #        (11, OBSIDIAN, 1),
        #        (15, OBSIDIAN, 2),
        #        (12, CLAY, 4),
        #        (5, CLAY, 1),
        #        (1, ORE, 1),
    ]

    total = 0
    for id, line in enumerate(lines, start=1):
        t = Foo(line, cut_points).dijkstra()
        total += id * t
        print("id", id, "t", t)

    return total


#    print(Foo(lines[1]).collect_geodes1())
#    return sum(Foo(line).collect_geodes1() for line in lines[:1])


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    .
    """
    ...


if __name__ == "__main__":
    data = load_input(__file__, 2022, "19")
    #    data = load_example(__file__, "19")
    print(part1(data))
#    print(part2(data))
