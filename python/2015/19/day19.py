from pathlib import Path


def read_data(filename):
    replacements = []
    f = open(filename)
    while True:
        line = f.readline()
        if line.isspace():
            break
        replacements.append(line.strip().split(' => '))
    molecule = f.readline().strip()
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


def part1(filename):
    """
    >>> part1(Path(__file__).parent / 'reference_a')
    4
    >>> part1(Path(__file__).parent / 'reference_b')
    7
    """
    replacements, molecule = read_data(filename)
    molecules = do_one_replacement(replacements, molecule)
    return len(molecules)


def part2():
    # Guessed my solution, as a DFS-approach stalled at around depth 190.
    pass


if __name__ == '__main__':
    print(part1('input'))
    print(part2())
