from aoc.util import example

MAN_KEYS = 'byr iyr eyr hgt hcl ecl pid'.split()
ECL = 'amb blu brn gry grn hzl oth'.split()


def check_part1(passport):
    for key in passport:
        if key == 'cid':
            continue
        if key not in MAN_KEYS:
            return False
    for key in MAN_KEYS:
        if key not in passport:
            return False
    return True


def check_byr(byr):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    year = int(byr)
    if year < 1920 or 2002 < year:
        raise


def check_iyr(iyr):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    year = int(iyr)
    if year < 2010 or 2020 < year:
        raise


def check_eyr(eyr):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    year = int(eyr)
    if year < 2020 or 2030 < year:
        raise


def check_hgt(hgt):
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


def check_hcl(hcl):
    """ hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f. """
    if len(hcl) == 7 and hcl.startswith('#'):
        int(hcl[1:], 16)
    else:
        raise


def check_ecl(ecl):
    if ecl not in ECL:
        raise


def check_pid(pid):
    if len(pid) != 9:
        raise
    int(pid)


def check_part2(passport):
    for key in passport:
        if key == 'cid':
            continue
        if key not in MAN_KEYS:
            return False
    for key in MAN_KEYS:
        if key not in passport:
            return False
    try:
        check_byr(passport['byr'])
        check_eyr(passport['eyr'])
        check_iyr(passport['iyr'])
        check_hgt(passport['hgt'])
        check_hcl(passport['hcl'])
        check_ecl(passport['ecl'])
        check_pid(passport['pid'])
    except Exception:
        return False
    return True


def run(lines, check):
    """
    >>> run(example(__file__, '4'), check_part1)
    2
    >>> run(example(__file__, '4'), check_part2)
    2
    """
    passports = []
    p = {}
    for line in lines:
        if not line.strip():
            passports.append(p)
            p = {}
        else:
            for k, v in [token.split(':') for token in line.split(' ')]:
                p[k] = v.strip()
    passports.append(p)
    return sum(check(passport) for passport in passports)


def part1(lines):
    return run(lines, check_part1)


def part2(lines):
    return run(lines, check_part2)
