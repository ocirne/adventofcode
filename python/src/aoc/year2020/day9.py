from aoc.util import load_example, load_input


def check(preamble, my_slice, total):
    for i in range(preamble):
        for j in range(i):
            if my_slice[i] + my_slice[j] == total:
                return True
    return False


def solve_part1(nums, preamble):
    for i in range(preamble, len(nums)):
        if not check(preamble, nums[i-preamble:i], nums[i]):
            return nums[i]


def part1(lines, preamble=25):
    """
    >>> part1(load_example(__file__, '9'), 5)
    127
    """
    nums = [int(i) for i in lines]
    return solve_part1(nums, preamble)


def search(nums, target):
    for start in range(len(nums)):
        for length in range(len(nums)):
            my_slice = nums[start:length]
            if sum(my_slice) == target:
                return my_slice
    raise Exception


def part2(lines, preamble=25):
    """
    >>> part2(load_example(__file__, '9'), 5)
    62
    """
    nums = [int(i) for i in lines]
    target = solve_part1(nums, preamble)

    result = search(nums, target)
    return min(result) + max(result)


if __name__ == "__main__":
    data = load_input(__file__, 2020, '9')
    print(part1(data))
    print(part2(data))
