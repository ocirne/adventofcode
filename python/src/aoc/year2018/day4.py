from aoc.util import load_example, load_input


def identify_guard(line):
    return line.split("#")[1].split(" ")[0]


def identify_time(line):
    return int(line.split("]")[0].split(":")[1])


def part1(lines):
    """
    >>> part1(load_example(__file__, '4'))
    240
    """
    most_sleepy = "521"
    minutes = [0 for _ in range(60)]
    sleep_times = {}
    asleep_time = 0
    guard = None
    for line in sorted(lines):
        if "Guard" in line:
            guard = identify_guard(line)
            if guard not in sleep_times:
                sleep_times[guard] = 0
            # else:
        # 		raise
        elif "falls asleep" in line:
            asleep_time = identify_time(line)
        elif "wakes up" in line:
            wakes_up_time = identify_time(line)
            sleep_times[guard] += wakes_up_time - asleep_time
            if guard == most_sleepy:
                for i in range(asleep_time, wakes_up_time):
                    minutes[i] += 1
        else:
            raise

    #    for guard, totalSleepTime in sleep_times.items():
    #        print(guard, "->", totalSleepTime)

    #    print("minutes", minutes)

    max_so_far = -1
    minute = -1
    for i in range(60):
        if minutes[i] > max_so_far:
            max_so_far = minutes[i]
            minute = i

    return int(most_sleepy) * minute


def part2(lines):
    """
    >>> part2(load_example(__file__, '4'))
    4455
    """
    all_sleep_times = {}
    asleep_time = 0
    guard = None
    for line in sorted(lines):
        if "Guard" in line:
            guard = identify_guard(line)
            if guard not in all_sleep_times:
                all_sleep_times[guard] = [0 for _ in range(60)]
        elif "falls asleep" in line:
            asleep_time = identify_time(line)
        elif "wakes up" in line:
            wakes_up_time = identify_time(line)
            for i in range(asleep_time, wakes_up_time):
                all_sleep_times[guard][i] += 1
        else:
            raise

    max_so_far = -1
    guard_so_far = "."
    index_so_far = -1
    for guard, sleepTimes in all_sleep_times.items():
        for i in range(60):
            if sleepTimes[i] > max_so_far:
                max_so_far = sleepTimes[i]
                guard_so_far = guard
                index_so_far = i

    return int(guard_so_far) * index_so_far


if __name__ == "__main__":
    data = load_input(__file__, 2018, "4")
    print(part1(data))
    print(part2(data))
