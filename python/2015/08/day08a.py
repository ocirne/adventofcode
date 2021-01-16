
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
