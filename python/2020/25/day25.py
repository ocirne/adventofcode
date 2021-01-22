
M = 20201227
S = 7


def decrypt(key):
    s = S
    e = 1
    while True:
        s = (s * S) % M
        e += 1
        if s == key:
            return e


def run(filename):
    data = open(filename, 'r').readlines()
    key1, key2 = (int(v) for v in data)
    e1 = decrypt(key1)
    e2 = decrypt(key2)
    return pow(S, e1*e2, M)


assert run('reference') == 14897079

print(run('input'))



if __name__ == '__main__':
    print(part1('input'))
    print(part2('input'))
