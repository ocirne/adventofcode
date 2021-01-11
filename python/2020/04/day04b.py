
MAN_KEYS = 'byr iyr eyr hgt hcl ecl pid'.split()

ECL = 'amb blu brn gry grn hzl oth'.split()


def checkByr(byr):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    year = int(byr)
    if year < 1920 or 2002 < year:
        raise


def checkIyr(iyr):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    year = int(iyr)
    if year < 2010 or 2020 < year:
        raise


def checkEyr(eyr):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    year = int(eyr)
    if year < 2020 or 2030 < year:
        raise


def checkHgt(hgt):
    """hgt (Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if hgt.endswith('cm'):
        height = int(hgt[:-2])
        if height < 150 or 193 < height:
            raise
    elif hgt.endswith('in'):
        height = int(hgt[:-2])
        if height < 59 or 76 < height:
            raise
    else:
        raise


def checkHcl(hcl):
    """ hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f. """
    if len(hcl) == 7 and hcl.startswith('#'):
        num = int(hcl[1:], 16)
    else:
        raise


def checkEcl(ecl):
    if ecl not in ECL:
        raise


def checkPid(pid):
    if len(pid) != 9:
        raise
    int(pid)


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
    try:
        checkByr(passport['byr'])
        checkEyr(passport['eyr'])
        checkIyr(passport['iyr'])
        checkHgt(passport['hgt'])
        checkHcl(passport['hcl'])
        checkEcl(passport['ecl'])
        checkPid(passport['pid'])
    except Exception:
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
