import re

from aoc.util import load_input, load_example


class Part:

    PART_PATTERN = re.compile(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")

    def __init__(self, line):
        x, m, a, s = map(int, self.PART_PATTERN.match(line).groups())
        self.registers = {"x": x, "m": m, "a": a, "s": s}

    def rating(self):
        return sum(self.registers.values())


class LessThanRule:
    def __init__(self, variable, value, next_workflow):
        self.variable = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.registers[self.variable] < self.value

    def anti(self):
        return GreaterThanRule(self.variable, self.value - 1, "anti")


class GreaterThanRule:
    def __init__(self, variable, value, next_workflow):
        self.category = variable
        self.value = int(value)
        self.next_workflow = next_workflow

    def match(self, part):
        return part.registers[self.category] > self.value

    def anti(self):
        return LessThanRule(self.category, self.value + 1, "anti")


class DirectRule:
    def __init__(self, next_workflow):
        self.next_workflow = next_workflow

    def match(self, _):
        return True


class Workflow:

    LESS_THAN_PATTERN = re.compile(r"([xmas])<(\d+):([ARa-z]+)")
    GREATER_THAN_PATTERN = re.compile(r"([xmas])>(\d+):([ARa-z]+)")

    def __init__(self, rules):
        self.rules = []
        for rule in rules.split(","):
            if self.LESS_THAN_PATTERN.match(rule):
                self.rules.append(LessThanRule(*self.LESS_THAN_PATTERN.match(rule).groups()))
            elif self.GREATER_THAN_PATTERN.match(rule):
                self.rules.append(GreaterThanRule(*self.GREATER_THAN_PATTERN.match(rule).groups()))
            elif rule == "A" or rule == "R":
                self.rules.append(DirectRule(rule))
            elif re.match(r"[a-z]+", rule):
                self.rules.append(DirectRule(rule))
            else:
                raise

    def process(self, part):
        for rule in self.rules:
            if rule.match(part):
                return rule.next_workflow
        raise


class Workflows:

    WORKFLOW_PATTERN = re.compile(r"([a-z]+)\{(.*)}")

    def __init__(self, lines):
        it = iter(lines)

        self.workflows = {}
        for line in it:
            if not line:
                break
            g = self.WORKFLOW_PATTERN.match(line)
            name, rules = g.groups()
            self.workflows[name] = Workflow(rules)

        self.parts = [Part(line) for line in it]

    def _handle_part(self, part):
        current_workflow = self.workflows["in"]
        while True:
            result = current_workflow.process(part)
            if result in ("A", "R"):
                return result
            current_workflow = self.workflows[result]

    def sum_accepted_parts(self):
        return sum(part.rating() for part in self.parts if self._handle_part(part) == "A")

    @staticmethod
    def _upper_bound(constraints, category):
        values = [rule.value for rule in constraints if isinstance(rule, LessThanRule) and rule.variable == category]
        return min(values) if values else 4001

    @staticmethod
    def _lower_bound(constraints, category):
        values = [rule.value for rule in constraints if isinstance(rule, GreaterThanRule) and rule.category == category]
        return max(values) if values else 0

    def _collect_result(self, collected_rules):
        total = 1
        for v in "xmas":
            lb, ub = self._lower_bound(collected_rules, v), self._upper_bound(collected_rules, v)
            assert lb < ub
            p = ub - lb - 1
            total *= p
        return total

    def dfs(self, current_node="in", i=0, constraints=None):
        if constraints is None:
            constraints = []
        if current_node == "A":
            return self._collect_result(constraints)
        if current_node == "R":
            return 0
        current_workflow = self.workflows[current_node]
        if i >= len(current_workflow.rules):
            raise
        current_rule = current_workflow.rules[i]
        # match
        total = self.dfs(current_rule.next_workflow, 0, constraints + [current_rule])
        # no match
        if i + 1 < len(current_workflow.rules):
            total += self.dfs(current_node, i + 1, constraints + [current_rule.anti()])
        return total


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    19114
    """
    workflows = Workflows(lines)
    return workflows.sum_accepted_parts()


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    167409079868000
    """
    workflows = Workflows(lines)
    return workflows.dfs()


if __name__ == "__main__":
    data = load_input(__file__, 2023, "19")
    print(part1(data))
    print(part2(data))
