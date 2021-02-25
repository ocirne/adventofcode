from dataclasses import dataclass


def read_boss(filename):
    f = open(filename)
    return (int(line.split(':')[1]) for line in f.readlines())


@dataclass
class Spell:
    name: str
    mana_cost: int
    boss_hit: int = 0
    player_hp: int = 0
    armor: int = 0
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0


SPELLS = [
    Spell('magic missile', 53, boss_hit=4),
    Spell('drain',         73, boss_hit=2, player_hp=2),
    Spell('shield',       113, armor=7, shield_timer=6),
    Spell('poison',       173, poison_timer=6),
    Spell('recharge',     229, recharge_timer=5),
]


class Node:
    def __init__(self, boss_hp, boss_da, hp, mana, hard, ar=0, st=0, pt=0, rt=0):
        self.boss_hp = boss_hp
        self.boss_da = boss_da
        self.hp = hp
        self.mana = mana
        self.hard = hard
        self.spell = None
        self.ar = ar
        self.st = st
        self.pt = pt
        self.rt = rt
        self.win = False
        self.parent = None
        self.G = 0
        self.cost = 0

    def copy(self):
        return Node(self.boss_hp, self.boss_da, self.hp, self.mana, self.hard, self.ar, self.st, self.pt, self.rt)

    def apply_effects(self):
        if self.st > 0:
            if self.st == 1:
                self.ar -= 7
            self.st -= 1
        if self.pt > 0:
            self.boss_hp -= 3
            self.pt -= 1
        if self.rt > 0:
            self.mana += 101
            self.rt -= 1

    def boss_damage_kills(self):
        self.hp -= max(1, self.boss_da - self.ar)
        return self.hp <= 0

    def check_win_condition(self):
        if self.boss_hp <= 0 < self.hp:
            self.win = True
        return self.win

    def next_spell(self, spell: Spell):
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        if node.mana <= spell.mana_cost:
            return None
        node.spell = spell.name
        node.mana -= spell.mana_cost
        node.boss_hp -= spell.boss_hit
        node.hp += spell.player_hp
        node.ar += spell.armor
        if spell.shield_timer > 0:
            if node.st > 0:
                return None
            node.st = spell.shield_timer
        if spell.poison_timer > 0:
            if node.pt > 0:
                return None
            node.pt = spell.poison_timer
        if spell.recharge_timer > 0:
            if node.rt > 0:
                return None
            node.rt = spell.recharge_timer
        node.cost = spell.mana_cost
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if node.boss_damage_kills():
            return None
        node.check_win_condition()
        return node


def next_spell(current: Node):
    return (node for node in (current.next_spell(spell) for spell in SPELLS) if node)


def search(start):
    open_set = set()
    result_list = []
    best_result = 2000
    current = start
    open_set.add(current)
    while open_set:
        current = min(open_set, key=lambda o: o.G)
        if current.win:
            path = []
            backtrack = current
            while backtrack.parent:
                path.append(backtrack)
                backtrack = backtrack.parent
            path.append(backtrack)
            result_list.append(path[::-1])
            best_result = min(sum(n.cost for n in p) for p in result_list)
        open_set.remove(current)
        for node in next_spell(current):
            node.G = current.G + current.cost
            if node.G < best_result:
                node.parent = current
                open_set.add(node)
    return result_list, best_result


def run(boss_hp, boss_da, hp, mana, hard=False):
    """
    >>> run(13, 8, 10, 250)
    poison -> magic missile
    226
    >>> run(14, 8, 10, 250, hard=False)
    recharge -> shield -> drain -> poison -> magic missile
    641
    """
    start = Node(boss_hp, boss_da, hp, mana, hard)
    results, best_result = search(start)
    for path in results:
        if best_result == sum(node.cost for node in path):
            print(' -> '.join(node.spell for node in path if node.spell))
    return best_result


if __name__ == '__main__':
    input_hp, input_da = read_boss('input')
    print(run(input_hp, input_da, 50, 500))
    print(run(input_hp, input_da, 50, 500, hard=True))
