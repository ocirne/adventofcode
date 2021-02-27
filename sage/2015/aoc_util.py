from pathlib import Path


def example(day):
    return open(Path(__file__).parent / ('examples/%s.txt' % day))
