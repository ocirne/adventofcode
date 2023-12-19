import re

from aoc.util import load_input, load_example


WORKFLOW_PATTERN = re.compile(r"([a-z]+)\{(.*)}")
LESS_THAN_PATTERN = re.compile(r"([xmas])<(\d+):([ARa-z]+)")
GREATER_THAN_PATTERN = re.compile(r"([xmas])>(\d+):([ARa-z]+)")
PART_PATTERN = re.compile(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")


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
        self.variable = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.foo[self.variable] > self.value

    def __str__(self) -> str:
        return self.variable + " greater than: " + str(self.value) + " -> " + self.next_workflow

    def anti(self):
        return LessThanRule(self.variable, self.value + 1, "anti")


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
                print("Problem", rule)
                raise

    def __str__(self) -> str:
        return "; ".join(str(s) for s in self.rules)

    def process(self, part):
        for rule in self.rules:
            if rule.match(part):
                return rule.next_workflow
        raise


class Part:
    def __init__(self, line):
        x, m, a, s = map(int, PART_PATTERN.match(line).groups())
        self.foo = {"x": x, "m": m, "a": a, "s": s}

    def sum(self):
        return sum(self.foo.values())


def handle_part(workflows, part):
    current_workflow = workflows["in"]
    while True:
        result = current_workflow.process(part)
        if result in ("A", "R"):
            return result
        current_workflow = workflows[result]


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    19114
    """
    it = iter(lines)

    workflows = {}
    for line in it:
        if not line:
            break
        g = WORKFLOW_PATTERN.match(line)
        name, rules = g.groups()
        workflows[name] = Workflow(rules)
        print("workflow", workflows[name])
    print()
    total = 0
    for line in it:
        print("part", line)
        part = Part(line)
        if handle_part(workflows, part) == "A":
            total += part.sum()
    return total


def upper_bound(collected_rules, variable):
    values = [rule.value for rule in collected_rules if isinstance(rule, LessThanRule) and rule.variable == variable]
    return min(values) if values else 4001


def lower_bound(collected_rules, variable):
    values = [rule.value for rule in collected_rules if isinstance(rule, GreaterThanRule) and rule.variable == variable]
    return max(values) if values else 0


def bar(collected_rules):
    total = 1
    for v in "xmas":
        lb, ub = lower_bound(collected_rules, v), upper_bound(collected_rules, v)
        assert lb < ub
        p = ub - lb - 1
        print(v, lb, ub, p)
        total *= p
    return total


def rec(workflows, current_node, i=0, collected_rules=[]):
    if current_node == "A":
        print("; ".join(str(s) for s in collected_rules))
        return bar(collected_rules)
    if current_node == "R":
        return 0
    current_workflow = workflows[current_node]
    if i >= len(current_workflow.rules):
        raise
    current_rule = current_workflow.rules[i]
    # match
    total = rec(workflows, current_rule.next_workflow, 0, collected_rules + [current_rule])
    # no match
    if i + 1 < len(current_workflow.rules):
        total += rec(workflows, current_node, i + 1, collected_rules + [current_rule.anti()])
    return total


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    167409079868000
    """
    it = iter(lines)

    workflows = {}
    for line in it:
        if not line:
            break
        g = WORKFLOW_PATTERN.match(line)
        name, rules = g.groups()
        workflows[name] = Workflow(rules)
    #        print("workflow", workflows[name])

    while True:
        direct = {}
        for name, workflow in workflows.items():
            targets = [rule.next_workflow for rule in workflow.rules]
            if len(set(targets)) == 1:
                direct[name] = targets[0]
        if not direct:
            break
        for name, workflow in workflows.items():
            for rule in workflow.rules:
                if rule.next_workflow in direct:
                    rule.next_workflow = direct[rule.next_workflow]
        for name in direct:
            workflows.pop(name)
    for name, wf in workflows.items():
        print(name, "; ".join(str(s) for s in wf.rules))

    print()
    # analyze workflow tree
    return rec(workflows, "in")


if __name__ == "__main__":
    data = load_input(__file__, 2023, "19")
    print(part1(data))
    print(part2(data))
