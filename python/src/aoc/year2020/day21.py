from collections import defaultdict
from aoc.util import example

INGREDIENTS_WITH_ALLERGENS_REFERENCE = ['mxmxvkd', 'sqjhc', 'fvjkl']

INGREDIENTS_WITH_ALLERGENS_INPUT = ['txdmlzd', 'mptbpz', 'vlblq', 'cxsvdm', 'rsbxb', 'xbnmzr', 'glf', 'mtnh']


def intersect(d):
    sets = iter(set(x) for x in d)
    return set.intersection(*sets)


def prepare_data(lines):
    data = defaultdict(list)
    for line in lines:
        ingredients_string, allergens_string = line.split(' (contains ')
        ingredients = ingredients_string.split()
        allergens = allergens_string.strip('\n)').split(', ')
        for allergen in allergens:
            data[allergen].append(ingredients)
    return data


def part1(lines, known_allergens=None):
    """
    >>> part1(example(__file__, '21'), INGREDIENTS_WITH_ALLERGENS_REFERENCE)
    5
    """
    if known_allergens is None:
        known_allergens = INGREDIENTS_WITH_ALLERGENS_INPUT
    total = 0
    for line in lines:
        ingredients = line.split(' (contains ')[0].split()
        total += len(set(ingredients).difference(set(known_allergens)))
    return total


def part2(lines):
    """
    >>> part2(example(__file__, '21'))
    'mxmxvkd,sqjhc,fvjkl'
    """
    data = prepare_data(lines)
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
