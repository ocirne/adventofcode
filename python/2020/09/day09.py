
def check(preamble, slice, total):
    for i in range(preamble):
        for j in range(i):
            if slice[i] + slice[j] == total:
                return True
    return False


def run(filename, preamble):
    f = open(filename, 'r')
    nums = list(map(int, f.readlines()))

    for i in range(preamble, len(nums)):
        if not check(preamble, nums[i-preamble:i], nums[i]):
            return nums[i]

if __name__ == '__main__':
    assert run('reference', 5) == 127

    print(run('input', 25))




if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))

import day09a


def search(nums, target):
    for start in range(len(nums)):
        for length in range(len(nums)):
            slice = nums[start:length]
            if sum(slice) == target:
                return slice
    raise Exception


def run(filename, preamble):
    target = day09a.run(filename, preamble)
    f = open(filename, 'r')
    nums = list(map(int, f.readlines()))

    result = search(nums, target)
    return min(result) + max(result)


assert run('reference', 5) == 62

print(run('input', 25))
