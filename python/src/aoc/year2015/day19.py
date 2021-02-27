from aoc.util import example


def prepare_data(lines):
    f = iter(lines)
    replacements = []
    while True:
        line = next(f)
        if line.isspace():
            break
        replacements.append(line.strip().split(' => '))
    molecule = next(f).strip()
    return replacements, molecule


def replace_at(molecule, old, index, new):
    return molecule[:index] + new + molecule[index + len(old):]


def generate_replacements(molecule, old, new):
    index = molecule.find(old)
    while index != -1:
        yield replace_at(molecule, old, index, new)
        index = molecule.find(old, index + 1)


def do_one_replacement(replacements, molecule: str):
    result = []
    for atom, replacement in replacements:
        result.extend(r for r in generate_replacements(molecule, atom, replacement))
    return set(result)


def part1(lines):
    """
    >>> part1(example(__file__, '19a'))
    4
    >>> part1(example(__file__, '19b'))
    7
    """
    replacements, molecule = prepare_data(lines)
    molecules = do_one_replacement(replacements, molecule)
    return len(molecules)


def part2():
    # Guessed my solution, as a DFS-approach stalled at around depth 190.
    pass
