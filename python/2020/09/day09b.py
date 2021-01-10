
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
