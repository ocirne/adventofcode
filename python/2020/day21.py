from collections import defaultdict
from pathlib import Path

INGREDIENTS_WITH_ALLERGENS_REFERENCE = ['mxmxvkd', 'sqjhc', 'fvjkl']

INGREDIENTS_WITH_ALLERGENS_INPUT = ['txdmlzd', 'mptbpz', 'vlblq', 'cxsvdm', 'rsbxb', 'xbnmzr', 'glf', 'mtnh']


def intersect(d):
    sets = iter(set(x) for x in d)
    return set.intersection(*sets)


def read_data(filename):
    f = open(filename)
    data = defaultdict(list)
    for line in f.readlines():
        ingredients_string, allergens_string = line.split(' (contains ')
        ingredients = ingredients_string.split()
        allergens = allergens_string.strip('\n)').split(', ')
        for allergen in allergens:
            data[allergen].append(ingredients)
    return data


def part1(filename, known_allergens):
    """
    >>> part1(Path(__file__).parent / 'reference', INGREDIENTS_WITH_ALLERGENS_REFERENCE)
    5
    """
    f = open(filename)
    total = 0
    for line in f.readlines():
        ingredients = line.split(' (contains ')[0].split()
        total += len(set(ingredients).difference(set(known_allergens)))
    return total


def part2(filename):
    """
    >>> part2(Path(__file__).parent / 'reference')
    'mxmxvkd,sqjhc,fvjkl'
    """
    data = read_data(filename)
    known_allergen = {}
    detected = True
    while detected:
        detected = False
        for allergen, ingredientLists in data.items():
            common = intersect(ingredientLists).difference(set(known_allergen.values()))
            if len(common) == 1:
                ingredient = list(common)[0]
                known_allergen[allergen] = ingredient
                detected = True
    return ','.join(known_allergen[key] for key in sorted(known_allergen))


if __name__ == '__main__':
    print(part1('input', INGREDIENTS_WITH_ALLERGENS_INPUT))
    print(part2('input'))
