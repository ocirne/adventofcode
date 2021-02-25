from pathlib import Path


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference_a')
    71
    """
    f = open(filename)
    d = set()
    line = f.readline()
    while not line.isspace():
        range1, _, range2 = line.split(':')[1].split()
        from1, to1 = (int(t) for t in range1.split('-'))
        from2, to2 = (int(t) for t in range2.split('-'))
        d.update(range(from1, to1+1))
        d.update(range(from2, to2+1))
        line = f.readline()
    for _ in range(4):
        f.readline()

    total = 0
    line = f.readline()
    while line and not line.isspace():
        nums = (int(t) for t in line.split(','))
        total += sum(i for i in nums if i not in d)
        line = f.readline()

    return total


def is_valid(ticket, all_ranges):
    for i in ticket:
        if i not in all_ranges:
            return False
    return True


def is_name_possible(index, tickets, my_range):
    for ticket in tickets:
        if ticket[index] not in my_range:
            return False
    return True


def find_fields(pinned, index, valid_tickets, ranges):
    result = []
    for name in ranges:
        if name in pinned.values():
            continue
        if is_name_possible(index, valid_tickets, ranges[name]):
            result.append(name)
    return result


def part2(filename):
    f = open(filename)
    ranges = {}
    line = f.readline()
    while not line.isspace():
        name, category_ranges = line.split(':')
        range1, _, range2 = category_ranges.split()
        from1, to1 = (int(t) for t in range1.split('-'))
        from2, to2 = (int(t) for t in range2.split('-'))
        valid_values = set()
        valid_values.update(range(from1, to1+1))
        valid_values.update(range(from2, to2+1))
        ranges[name] = valid_values
        line = f.readline()

    all_ranges = list(set().union(*ranges.values()))

    f.readline()
    my_ticket = [int(i) for i in f.readline().split(',')]
    f.readline()
    f.readline()

    valid_tickets = []
    line = f.readline()
    while line and not line.isspace():
        ticket = [int(t) for t in line.split(',')]
        if is_valid(ticket, all_ranges):
            valid_tickets.append(ticket)
        line = f.readline()

    pinned = {}
    while len(pinned) < len(my_ticket):
        for i in range(len(my_ticket)):
            possible_fields = find_fields(pinned, i, valid_tickets, ranges)
            if len(possible_fields) == 1:
                pinned[i] = possible_fields[0]

    answer = 1
    for i in sorted(pinned):
        if pinned[i].startswith('departure'):
            answer *= my_ticket[i]
    return answer


if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
