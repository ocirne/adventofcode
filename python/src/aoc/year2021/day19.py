from itertools import combinations

from aoc.util import load_input, load_example


def read_data(lines):
    base_cubes = []
    cube = []
    for line in lines[1:]:
        if not line.strip():
            continue
        elif "scanner" in line:
            base_cubes.append(cube)
            cube = []
        else:
            cube.append(tuple(map(int, line.split(","))))
    base_cubes.append(cube)
    return base_cubes


# https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array


def roll(v):
    return v[0], v[2], -v[1]


def turn(v):
    return -v[1], v[0], v[2]


def rotations(v):
    for _ in range(2):
        for _ in range(3):
            v = roll(v)
            yield v
            for _ in range(3):
                v = turn(v)
                yield v
        v = roll(turn(roll(v)))


def rotate_base_cubes(base_cubes):
    rotated_cubes = []
    for base_cube in base_cubes[1:]:
        rotated_cube = [[] for _ in range(24)]
        for xyz in base_cube:
            for j, r in enumerate(rotations(xyz)):
                rotated_cube[j].append(r)
        rotated_cubes.append(rotated_cube)
    # first cube is not rotated
    return base_cubes[0], rotated_cubes


def transform(cube, dx, dy, dz):
    return [(x + dx, y + dy, z + dz) for x, y, z in cube]


def find_overlap(cube1, cube2):
    for x1, y1, z1 in cube1:
        for x2, y2, z2 in cube2:
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
            transformed_cube2 = transform(cube2, dx, dy, dz)
            beacons = set(cube1).intersection(set(transformed_cube2))
            if len(beacons) >= 12:
                return transformed_cube2, (dx, dy, dz)
    return None, None


def solve(fixed_cube, rotated_cubes):
    known_cubes = [fixed_cube]
    open_list = rotated_cubes
    scanners = []
    while open_list:
        for known in known_cubes:
            for rotations in open_list:
                for r in rotations:
                    transformed_cube, scanner = find_overlap(known, r)
                    if transformed_cube is not None:
                        known_cubes.append(transformed_cube)
                        scanners.append(scanner)
                        open_list.remove(rotations)
    return set().union(*known_cubes), scanners


def find_all_beacons(lines):
    base_cubes = read_data(lines)
    fixed_cube, rotated_cubes = rotate_base_cubes(base_cubes)
    return solve(fixed_cube, rotated_cubes)


def part1(lines):
    """
    >>> part1(load_example(__file__, "19"))
    79
    """
    return len(find_all_beacons(lines)[0])


def manhattan_distance(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1]) + abs(u[2] - v[2])


def part2(lines):
    """
    >>> part2(load_example(__file__, "19"))
    3621
    """
    scanners = find_all_beacons(lines)[1]
    return max(manhattan_distance(s1, s2) for s1, s2 in combinations(scanners, 2))


if __name__ == "__main__":
    assert part1(load_example(__file__, "19")) == 79
    assert part2(load_example(__file__, "19")) == 3621
    data = load_input(__file__, 2021, "19")
    #    print(part1(data))
    print(part2(data))
