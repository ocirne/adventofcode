
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
