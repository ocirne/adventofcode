
def read_boss(filename):
    f = open(filename, 'r')
    return (int(line.split(':')[1]) for line in f.readlines())


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

    def magic_missile(self):
        """ Magic Missile costs 53 mana. It instantly does 4 damage. """
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        node.spell = 'magic missile'
        if not node.win and node.mana <= 53:
            return None
        node.mana -= 53
        node.boss_hp -= 4
        node.cost = 53
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if not node.win and node.boss_damage_kills():
            return None
        if node.check_win_condition():
            return node
        return node

    def drain(self):
        """ Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points. """
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        node.spell = 'drain'
        if not node.win and node.mana <= 73:
            return None
        node.mana -= 73
        node.boss_hp -= 2
        node.hp += 2
        node.cost = 73
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if not node.win and node.boss_damage_kills():
            return None
        if node.check_win_condition():
            return node
        return node

    def shield(self):
        """ Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is
            increased by 7.
        """
        if self.st > 1:
            return None
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        node.spell = 'shield'
        if not node.win and node.mana <= 113:
            return None
        node.mana -= 113
        node.ar += 7
        node.st = 6
        node.cost = 113
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if not node.win and node.boss_damage_kills():
            return None
        if node.check_win_condition():
            return node
        return node

    def poison(self):
        """ Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is
            active, it deals the boss 3 damage.
        """
        if self.pt > 1:
            return None
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        node.spell = 'poison'
        if not node.win and node.mana <= 173:
            return None
        node.mana -= 173
        node.pt = 6
        node.cost = 173
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if not node.win and node.boss_damage_kills():
            return None
        if node.check_win_condition():
            return node
        return node

    def recharge(self):
        """ Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is
            active, it gives you 101 new mana.
        """
        if self.rt > 1:
            return None
        node = self.copy()
        if node.hard:
            node.hp -= 1
            if node.hp <= 0:
                return None
        node.apply_effects()
        if node.check_win_condition():
            return node
        node.spell = 'recharge'
        if not node.win and node.mana <= 229:
            return None
        node.mana -= 229
        node.rt = 5
        node.cost = 229
        if node.check_win_condition():
            return node
        node.apply_effects()
        if node.check_win_condition():
            return node
        if not node.win and node.boss_damage_kills():
            return None
        if node.check_win_condition():
            return node
        return node


def next_spell(current: Node):
    if current.hp <= 0 or current.mana <= 0:
        return []
    return [node for node in (current.magic_missile(), current.drain(), current.shield(), current.poison(),
                              current.recharge()) if node]


def dijkstra(start):
    open_set = set()
    result_list = []
    best_result = 2000
    current = start
    open_set.add(current)
    while open_set:
        current = min(open_set, key=lambda o: o.G)
        if current.win:  # player wins
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
    results, best_result = dijkstra(start)
    for path in results:
        if best_result == sum(node.cost for node in path):
            print(' -> '.join(node.spell for node in path if node.spell))
    return best_result


if __name__ == '__main__':
    input_hp, input_da = read_boss('input')
    print(run(input_hp, input_da, 50, 500))
    print(run(input_hp, input_da, 50, 500, hard=True))
