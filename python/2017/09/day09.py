
def run(stream):
    """
    >>> run('{}')[0]
    1
    >>> run('{{{}}}')[0]
    6
    >>> run('{{},{}}')[0]
    5
    >>> run('{{{},{},{{}}}}')[0]
    16
    >>> run('{<a>,<a>,<a>,<a>}')[0]
    1
    >>> run('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0]
    9
    >>> run('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0]
    9
    >>> run('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0]
    3

    >>> run('<>')[1]
    0
    >>> run('<random characters>')[1]
    17
    >>> run('<<<<>')[1]
    3
    >>> run('<{!>}>')[1]
    2
    >>> run('<!!>')[1]
    0
    >>> run('<!!!>>')[1]
    0
    >>> run('<{o"i!a,<{i<a>')[1]
    10
    """
    i = 0
    depth = 0
    garbage = False
    count_garbage = 0
    count_groups = 0
    while i < len(stream):
        c = stream[i]
        i += 1
        if c == '!':
            i += 1
            continue
        if c == '>':
            garbage = False
        if garbage:
            count_garbage += 1
            continue
        if c == '<':
            garbage = True
        if c == '{':
            depth += 1
        if c == '}':
            count_groups += depth
            depth -= 1
    return count_groups, count_garbage


if __name__ == '__main__':
    input_data = open('input', 'r').readline().strip()
    answer1, answer2 = run(input_data)
    print(answer1)
    print(answer2)
