from pathlib import Path


def check(preamble, my_slice, total):
    for i in range(preamble):
        for j in range(i):
            if my_slice[i] + my_slice[j] == total:
                return True
    return False


def part1(filename, preamble):
    """
    >>> part1(Path(__file__).parent / 'reference', 5)
    127
    """
    f = open(filename)
    nums = list(map(int, f.readlines()))

    for i in range(preamble, len(nums)):
        if not check(preamble, nums[i-preamble:i], nums[i]):
            return nums[i]


def search(nums, target):
    for start in range(len(nums)):
        for length in range(len(nums)):
            my_slice = nums[start:length]
            if sum(my_slice) == target:
                return my_slice
    raise Exception


def part2(filename, preamble):
    """
    >>> part2(Path(__file__).parent / 'reference', 5)
    62
    """
    target = part1(filename, preamble)
    f = open(filename)
    nums = list(map(int, f.readlines()))

    result = search(nums, target)
    return min(result) + max(result)


if __name__ == '__main__':
    print(part1('input', 25))
    print(part2('input', 25))
