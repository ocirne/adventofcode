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
        return self.variable + " less than: " + self.value + " -> " + self.next_workflow


class GreaterThanRule:
    def __init__(self, variable, value, next_workflow):
        self.variable = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.foo[self.variable] > self.value

    def __str__(self) -> str:
        return self.variable + " greater than: " + self.value + " -> " + self.next_workflow


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
        return str(self.rules)

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


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    """


if __name__ == "__main__":
    # print(part1(load_example(__file__, "19")))
    data = load_input(__file__, 2023, "19")
    print(part1(data))
    # print(part2(data))
