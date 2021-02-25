import math
from dataclasses import dataclass
from itertools import combinations, chain


@dataclass
class Equipment:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Stats:
    hit_points: int
    damage: int
    armor: int


WEAPONS = [
    Equipment('Dagger', 8, 4, 0),
    Equipment('Shortsword', 10, 5, 0),
    Equipment('Warhammer', 25, 6, 0),
    Equipment('Longsword', 40, 7, 0),
    Equipment('Greataxe', 74, 8, 0),
]

ARMOR = [
    Equipment('Leather', 13, 0, 1),
    Equipment('Chainmail', 31, 0, 2),
    Equipment('Splintmail', 53, 0, 3),
    Equipment('Bandedmail', 75, 0, 4),
    Equipment('Platemail', 102, 0, 5),
]

RINGS = [
    Equipment('Damage +1', 25, 1, 0),
    Equipment('Damage +2', 50, 2, 0),
    Equipment('Damage +3', 100, 3, 0),
    Equipment('Defense +1', 20, 0, 1),
    Equipment('Defense +2', 40, 0, 2),
    Equipment('Defense +3', 80, 0, 3),
]


def read_boss_stats(filename):
    f = open(filename)
    return Stats(*(int(line.split(':')[1]) for line in f.readlines()))


def pick(von, bis, equipment: list):
    for i in range(von, bis):
        for c in combinations(equipment, i):
            yield c


def first_wins(player, boss):
    needed_player_hits = math.ceil(boss.hit_points / max(1, player.damage - boss.armor))
    needed_boss_hits = math.ceil(player.hit_points / max(1, boss.damage - player.armor))
    return needed_player_hits <= needed_boss_hits


def player_wins(player, boss):
    return first_wins(player, boss)


def boss_wins(player, boss):
    return first_wins(boss, player)


def all_fights(boss, who_wins):
    for weapon in pick(1, 2, WEAPONS):
        for armor in pick(0, 2, ARMOR):
            for rings in pick(0, 3, RINGS):
                total_damage = sum(eq.damage for eq in chain.from_iterable([weapon, armor, rings]))
                total_armor = sum(eq.armor for eq in chain.from_iterable([weapon, armor, rings]))
                player = Stats(100, total_damage, total_armor)
                if who_wins(player, boss):
                    yield sum(eq.cost for eq in chain.from_iterable([weapon, armor, rings]))


def part1(boss):
    return min(all_fights(boss, player_wins))


def part2(boss):
    return max(all_fights(boss, boss_wins))


if __name__ == '__main__':
    inputBoss = read_boss_stats('input')
    print(part1(inputBoss))
    print(part2(inputBoss))
