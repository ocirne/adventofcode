from collections import defaultdict

from aoc.util import load_example, load_input


def identify_guard(line):
    return int(line.split("#")[1].split(" ")[0])


def identify_time(line):
    return int(line.split("]")[0].split(":")[1])


def read_sleep_times(lines):
    all_sleep_times = defaultdict(lambda: [0 for _ in range(60)])
    asleep_time = 0
    guard = None
    for line in sorted(lines):
        if "Guard" in line:
            guard = identify_guard(line)
        elif "falls asleep" in line:
            asleep_time = identify_time(line)
        elif "wakes up" in line:
            wakes_up_time = identify_time(line)
            for i in range(asleep_time, wakes_up_time):
                all_sleep_times[guard][i] += 1
    return all_sleep_times


def find_most_sleepy_guard(all_sleep_times):
    return max(
        (sum(all_sleep_times[guard][minute] for minute in range(60)), guard) for guard in all_sleep_times.keys()
    )[1]


def find_most_sleepy_minute(all_sleep_times, guard):
    return max((all_sleep_times[guard][minute], minute) for minute in range(60))[1]


def part1(lines):
    """
    >>> part1(load_example(__file__, '4'))
    240
    """
    all_sleep_times = read_sleep_times(lines)
    guard = find_most_sleepy_guard(all_sleep_times)
    minute = find_most_sleepy_minute(all_sleep_times, guard)
    return guard * minute


def find_most_frequently_asleep_guard(all_sleep_times):
    return max(
        (all_sleep_times[guard][minute], guard, minute) for guard in all_sleep_times.keys() for minute in range(60)
    )[1:]


def part2(lines):
    """
    >>> part2(load_example(__file__, '4'))
    4455
    """
    all_sleep_times = read_sleep_times(lines)
    guard, minute = find_most_frequently_asleep_guard(all_sleep_times)
    return guard * minute


if __name__ == "__main__":
    data = load_input(__file__, 2018, "4")
    print(part1(data))
    print(part2(data))
