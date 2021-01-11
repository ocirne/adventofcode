
MAN_KEYS = 'byr iyr eyr hgt hcl ecl pid'.split()


def check(passport):
    for key in passport:
        if key == 'cid':
            continue
        if key not in MAN_KEYS:
            print(key, passport)
            return False
    for key in MAN_KEYS:
        if key not in passport:
            return False
    return True


def run(filename):
    f = open(filename, 'r')
    passports = []
    p = {}
    for line in f.readlines():
        if not line.strip():
            passports.append(p)
            p = {}
        else:
            for k, v in [token.split(':') for token in line.split(' ')]:
                p[k] = v.strip()
    passports.append(p)

    return sum(check(passport) for passport in passports)


assert run('reference') == 2

print(run('input'))
