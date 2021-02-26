
def play(nth, *start_values):
    """
    >>> play(2020, 0, 3, 6)
    436
    >>> play(2020, 1, 3, 2)
    1
    >>> play(2020, 2, 1, 3)
    10
    >>> play(2020, 1, 2, 3)
    27
    >>> play(2020, 2, 3, 1)
    78
    >>> play(2020, 3, 2, 1)
    438
    >>> play(2020, 3, 1, 2)
    1836
    """
    d = {value: startIndex for startIndex, value in enumerate(start_values)}
    value, next_value = 0, 0
    for index in range(len(start_values), nth):
        value = next_value
        if value in d:
            next_value = index - d[value]
        else:
            next_value = 0
        d[value] = index
    return value


if __name__ == '__main__':
    input_data = [int(t) for t in open('input').readline().split(',')]
    print(play(2020, *input_data))
    print(play(30000000, *input_data))
