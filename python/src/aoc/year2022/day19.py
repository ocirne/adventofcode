from collections import defaultdict

from aoc.util import load_input, load_example
import re

from constantly import NamedConstant, ValueConstant

BLUEPRINT_PATTERN = re.compile(
    r"^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$"  # noqa: E501
)

ORE = ValueConstant("ore")
CLAY = ValueConstant("clay")
OBSIDIAN = ValueConstant("obsidian")
GEODE = ValueConstant("geode")
FINISH = NamedConstant()

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


class Foo:
    def __init__(self, line):
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

    def dfs(self, phase, minute, minerals, robots, new_robot):
        if minute < 0:
            #            print(', '.join("%s: %s" % (key.value, value) for key, value in minerals.items()))
            self.best_can_do = max(self.best_can_do, minerals[GEODE])
            return
        minerals = minerals.copy()
        robots = robots.copy()
        # build new robots
        if phase == GEODE:
            if (
                new_robot is None
                and minerals[ORE] >= self.geode_ore_cost
                and minerals[OBSIDIAN] >= self.geode_obsidian_cost
            ):
                minerals[ORE] -= self.geode_ore_cost
                minerals[OBSIDIAN] -= self.geode_obsidian_cost
                self.dfs(OBSIDIAN, minute, minerals, robots, GEODE)
            self.dfs(OBSIDIAN, minute, minerals, robots, new_robot)

        elif phase == OBSIDIAN:
            if (
                new_robot is None
                and minerals[ORE] >= self.obsidian_ore_cost
                and minerals[CLAY] >= self.obsidian_clay_cost
            ):
                minerals[ORE] -= self.obsidian_ore_cost
                minerals[CLAY] -= self.obsidian_clay_cost
                self.dfs(CLAY, minute, minerals, robots, OBSIDIAN)
            self.dfs(CLAY, minute, minerals, robots, new_robot)

        elif phase == CLAY:
            if new_robot is None and minerals[ORE] >= self.clay_ore_cost:
                minerals[ORE] -= self.clay_ore_cost
                self.dfs(ORE, minute, minerals, robots, CLAY)
            self.dfs(ORE, minute, minerals, robots, new_robot)

        elif phase == ORE:
            if new_robot is None and minerals[ORE] >= self.ore_ore_cost:
                minerals[ORE] -= self.ore_ore_cost
                self.dfs(FINISH, minute, minerals, robots, ORE)
            self.dfs(FINISH, minute, minerals, robots, new_robot)

        elif phase == FINISH:
            # collecting
            for r in resource:
                if robots[r] > 0:
                    minerals[r] += robots[r]
            # new robots
            if new_robot is not None:
                robots[new_robot] += 1
            self.dfs(GEODE, minute - 1, minerals, robots, None)

    def collect_geodes1(self):
        minerals = {r: 0 for r in resource}
        robots = {r: 0 for r in resource}
        robots[ORE] = 1
        new_robot = None

        self.dfs(GEODE, 24, minerals, robots, new_robot)
        return self.index * self.best_can_do


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    .
    """
    print(Foo(lines[0]).collect_geodes1())


#    print(Foo(lines[1]).collect_geodes1())
#    return sum(Foo(line).collect_geodes1() for line in lines[:1])


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    .
    """
    ...


if __name__ == "__main__":
    #    data = load_input(__file__, 2022, "19")
    data = load_example(__file__, "19")
    print(part1(data))
    print(part2(data))
