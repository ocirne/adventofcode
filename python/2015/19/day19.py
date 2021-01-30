from pathlib import Path


def read_data(filename):
    replacements = []
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if line.isspace():
            break
        replacements.append(line.strip().split(' => '))
    molecule = f.readline().strip()
    return replacements, molecule


def replace_at(molecule, atom, index, replacement):
    return molecule[:index] + replacement + molecule[index + len(atom):]


def do_one_replacement(replacements, molecule: str):
    result = []
    for atom, replacement in replacements:
        index = molecule.find(atom)
        while index != -1:
            result.append(replace_at(molecule, atom, index, replacement))
            index = molecule.find(atom, index + 1)
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


if __name__ == '__main__':
    print(part1('input'))
