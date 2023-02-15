from aoc.util import load_example, load_input


def prepare_data(lines):
    f = iter(lines)
    replacements = []
    while True:
        line = next(f)
        if not line:
            break
        replacements.append(line.split(" => "))
    molecule = next(f)
    return replacements, molecule


def replace_at(molecule, old, index, new):
    return molecule[:index] + new + molecule[index + len(old) :]


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
    >>> part1(load_example(__file__, '19a'))
    4
    >>> part1(load_example(__file__, '19b'))
    7
    """
    replacements, molecule = prepare_data(lines)
    molecules = do_one_replacement(replacements, molecule)
    return len(molecules)


def part2(lines):
    # Guessed my solution, as a DFS-approach stalled at around depth 190.
    pass


if __name__ == "__main__":
    data = load_input(__file__, 2015, "19")
    print(part1(data))
    print(part2(data))
