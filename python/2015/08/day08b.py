
def count(line):
    result = 0
    index = 0
    while index < len(line):
        character = line[index]
        if character == '"':
            result += 2
        elif character == '\\':
            result += 2
        elif character == '"':
            result += 3
        else:
            result += 1
        index += 1
    return result + 2


def run(filename):
    f = open(filename, 'r')
    before, after = 0, 0
    for line in map(str.strip, f.readlines()):
        before += len(line)
        after += count(line)
        print(before, after)
    return after - before


assert run('reference') == 19

print(run('input'))
