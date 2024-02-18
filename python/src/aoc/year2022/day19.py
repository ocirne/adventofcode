from heapq import heappush, heappop
from math import prod

from aoc.util import load_input, load_example
import re


BLUEPRINT_PATTERN = re.compile(
    r"^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$"  # noqa: E501
)

ORE = 3
CLAY = 2
OBSIDIAN = 1
GEODE = 0


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


class CollectingRobots:
    def __init__(self, line, target, relax=0):
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
        self.best_geodes = {0: 0}
        self.target = target
        self.relax = relax

    def find_neighbors(self, node: Node):
        if node.minute == self.target:
            if self.best_can_do < node.minerals[GEODE]:
                self.best_can_do = node.minerals[GEODE]
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

    def dijkstra(self):
        open_heap = []
        closed_set = set()
        heappush(open_heap, Node(0, (0, 0, 0, 0), (0, 0, 0, 1), set()))
        while open_heap:
            current = heappop(open_heap)
            #            print(len(open_heap), current.minute)
            if current.minerals[GEODE] < self.best_geodes[current.minute] - self.relax:
                continue
            if current.minute > self.target:
                raise
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


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    33
    """
    return sum(
        blueprint_id * CollectingRobots(blueprint, 24).dijkstra()
        for blueprint_id, blueprint in enumerate(lines, start=1)
    )


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    3472
    """
    return prod(CollectingRobots(blueprint, 32, relax=2).dijkstra() for blueprint in lines[:3])


if __name__ == "__main__":
    data = load_input(__file__, 2022, "19")
    print(part1(data))
    print(part2(data))
