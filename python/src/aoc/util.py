from pathlib import Path
from typing import List


def load_example(file_ref: str, day: str) -> List[str]:
    return open(Path(file_ref).parent / ("examples/%s.txt" % day)).readlines()


def load_input(file_ref: str, year: int, day: str) -> List[str]:
    return open(Path(file_ref).parent / ("../../../tests/resources/%s/%s/input" % (year, day))).readlines()
