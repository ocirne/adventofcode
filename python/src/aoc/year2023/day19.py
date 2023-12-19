import re

from aoc.util import load_input, load_example


WORKFLOW_PATTERN = re.compile(r"([a-z]+)\{(.*)}")
LESS_THAN_PATTERN = re.compile(r"([xmas])<(\d+):([ARa-z]+)")
GREATER_THAN_PATTERN = re.compile(r"([xmas])>(\d+):([ARa-z]+)")


class LessThanRule:
    def __init__(self, variable, value, next_workflow):
        self.variable = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.foo[self.variable] < self.value

    def __str__(self) -> str:
        return self.variable + " less than: " + str(self.value) + " -> " + self.next_workflow

    def anti(self):
        return GreaterThanRule(self.variable, self.value - 1, "anti")


class GreaterThanRule:
    def __init__(self, variable, value, next_workflow):
        self.category = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.foo[self.category] > self.value

    def __str__(self) -> str:
        return self.category + " greater than: " + str(self.value) + " -> " + self.next_workflow

    def anti(self):
        return LessThanRule(self.category, self.value + 1, "anti")


class DirectRule:
    def __init__(self, next_workflow):
        self.next_workflow = next_workflow

    def match(self, _):
        return True

    def __str__(self) -> str:
        return "Direct: " + self.next_workflow


class Workflow:
    def __init__(self, rules):
        self.rules = []
        for rule in rules.split(","):
            if LESS_THAN_PATTERN.match(rule):
                self.rules.append(LessThanRule(*LESS_THAN_PATTERN.match(rule).groups()))
            elif GREATER_THAN_PATTERN.match(rule):
                self.rules.append(GreaterThanRule(*GREATER_THAN_PATTERN.match(rule).groups()))
            elif rule == "A" or rule == "R":
                self.rules.append(DirectRule(rule))
            elif re.match(r"[a-z]+", rule):
                self.rules.append(DirectRule(rule))
            else:
                raise

    def __str__(self) -> str:
        return "; ".join(str(s) for s in self.rules)

    def process(self, part):
        for rule in self.rules:
            if rule.match(part):
                return rule.next_workflow
        raise


class Part:

    PART_PATTERN = re.compile(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")

    def __init__(self, line):
        x, m, a, s = map(int, self.PART_PATTERN.match(line).groups())
        self.foo = {"x": x, "m": m, "a": a, "s": s}

    def rating(self):
        return sum(self.foo.values())


def handle_part(workflows, part):
    current_workflow = workflows["in"]
    while True:
        result = current_workflow.process(part)
        if result in ("A", "R"):
            return result
        current_workflow = workflows[result]


def read_workflows_parts(lines):
    it = iter(lines)

    workflows = {}
    for line in it:
        if not line:
            break
        g = WORKFLOW_PATTERN.match(line)
        name, rules = g.groups()
        workflows[name] = Workflow(rules)

    parts = [Part(line) for line in it]

    return workflows, parts


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    19114
    """
    workflows, parts = read_workflows_parts(lines)
    return sum(part.rating() for part in parts if handle_part(workflows, part) == "A")


def upper_bound(constraints, category):
    values = [rule.value for rule in constraints if isinstance(rule, LessThanRule) and rule.variable == category]
    return min(values) if values else 4001


def lower_bound(constraints, category):
    values = [rule.value for rule in constraints if isinstance(rule, GreaterThanRule) and rule.category == category]
    return max(values) if values else 0


def bar(collected_rules):
    total = 1
    for v in "xmas":
        lb, ub = lower_bound(collected_rules, v), upper_bound(collected_rules, v)
        assert lb < ub
        p = ub - lb - 1
        total *= p
    return total


def dfs(workflows, current_node, i=0, constraints=[]):
    if current_node == "A":
        return bar(constraints)
    if current_node == "R":
        return 0
    current_workflow = workflows[current_node]
    if i >= len(current_workflow.rules):
        raise
    current_rule = current_workflow.rules[i]
    # match
    total = dfs(workflows, current_rule.next_workflow, 0, constraints + [current_rule])
    # no match
    if i + 1 < len(current_workflow.rules):
        total += dfs(workflows, current_node, i + 1, constraints + [current_rule.anti()])
    return total


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    167409079868000
    """
    workflows, _ = read_workflows_parts(lines)
    return dfs(workflows, "in")


if __name__ == "__main__":
    data = load_input(__file__, 2023, "19")
    print(part1(data))
    print(part2(data))
