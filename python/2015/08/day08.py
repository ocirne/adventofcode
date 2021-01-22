
def count(line):
    result = 0
    index = 0
    while index < len(line):
        character = line[index]
        if character == '"' and (index == 0 or index + 1 == len(line)):
            pass
        else:
            if character == '\\':
                if line[index+1] == '\\':
                    index += 1
                elif line[index+1] == '"':
                    index += 1
                elif line[index+1] == 'x' and line[index+2].isascii() and line[index+3].isascii():
                    index += 3
                else:
                    raise
            result += 1
        index += 1
    return result


def run(filename):
    f = open(filename, 'r')
    before, after = 0, 0
    for line in map(str.strip, f.readlines()):
        before += len(line)
        after += count(line)
    return before - after


assert run('reference') == 12

print(run('input'))




if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

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
