import csv
from pathlib import Path
from typing import List


def load_example(file_ref: str, day: str) -> List[str]:
    return open(Path(file_ref).parent / ("examples/%s.txt" % day)).readlines()


def load_input(file_ref: str, year: int, day: str) -> List[str]:
    return open(Path(file_ref).parent / ("../../../tests/resources/%s/%s/input" % (year, day))).readlines()


class AocTestUtil:
    def __init__(self, year):
        self.year = year
        self.test_data = {}
        with open(Path(__file__).parent / ("../../tests/resources/results%s.csv" % year), newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                day, part1, part2 = row["day"], row["part1"], row["part2"]
                self.test_data[int(day)] = part1, part2

    def run(self, day, fun, part):
        lines = open(Path(__file__).parent / ("../../tests/resources/%s/%s/input" % (self.year, day))).readlines()
        return str(fun(lines)), self.test_data[day][part - 1]
