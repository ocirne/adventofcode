
def shrink(line):
    """
    >>> shrink('""')
    (2, 0)
    >>> shrink('"abc"')
    (5, 3)
    >>> shrink('"aaa\\\\"aaa"')
    (10, 7)
    >>> shrink('"\\\\x27"')
    (6, 1)
    """
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
    return len(line), result


def expand(line):
    """
    >>> expand('""')
    (6, 2)
    >>> expand('"abc"')
    (9, 5)
    >>> expand('"aaa\\\\"aaa"')
    (16, 10)
    >>> expand('"\\\\x27"')
    (11, 6)
    """
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
    return result + 2, len(line)


def loop_sum(data, fun):
    greater, lower = 0, 0
    for line in map(str.strip, data):
        gre, low = fun(line)
        greater += gre
        lower += low
    return greater - lower


if __name__ == '__main__':
    inputData = open('input', 'r').readlines()
    print(loop_sum(inputData, shrink))
    print(loop_sum(inputData, expand))
