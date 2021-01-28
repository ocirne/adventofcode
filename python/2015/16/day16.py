
WRAPPING = {'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
            }
GREATER_THAN_ITEMS = ['cats', 'trees']
FEWER_THAN_ITEMS = ['pomeranians', 'goldfish']


def read_data(filename):
    result = []
    f = open(filename, 'r')
    for line in f.readlines():
        _, things_part = line.split(': ', 1)
        things = {}
        for thing in things_part.split(', '):
            key, value = thing.split(': ')
            things[key] = int(value)
        result.append(things)
    return result


def can_be1(things):
    for key, value in WRAPPING.items():
        if key in things and value != things[key]:
            return False
    return True


def can_be2(things):
    for key, value in WRAPPING.items():
        if key in things:
            if key in GREATER_THAN_ITEMS:
                if value > things[key]:
                    return False
            elif key in FEWER_THAN_ITEMS:
                if value < things[key]:
                    return False
            else:
                if value != things[key]:
                    return False
    return True


def run(filename, can_be, exclude=None):
    data = read_data(filename)
    for sue_no, things in enumerate(data):
        if can_be(things):
            if sue_no + 1 == exclude:
                continue
            return sue_no + 1


if __name__ == '__main__':
    answer1 = run('input', can_be1)
    answer2 = run('input', can_be2, answer1)
    print(answer1)
    print(answer2)
