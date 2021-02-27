from pathlib import Path
from typing import TextIO


def example(file_ref: str, day: str) -> TextIO:
    return open(Path(file_ref).parent / ('examples/%s.txt' % day))
