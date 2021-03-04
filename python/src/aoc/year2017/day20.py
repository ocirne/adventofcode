import re
from dataclasses import dataclass
from itertools import combinations

from aoc.util import load_input, load_example


def part1(lines):
    r""" ¯\_(ツ)_/¯ """
    return next(index for index, line in enumerate(lines) if "a=<0,0,0>" in line)


@dataclass
class Particle:
    position: tuple
    velocity: tuple
    acceleration: tuple


def e(triple):
    return (int(t) for t in triple.split(","))


def prepare_data(lines):
    particle_matcher = re.compile(r"p=<(.*)>, v=<(.*)>, a=<(.*)>")
    particles = []
    for line in lines:
        m = particle_matcher.match(line)
        particles.append(Particle(*(e(g) for g in m.groups())))
    return particles


def simulate(particles):
    result = []
    for p in particles:
        px, py, pz = p.position
        vx, vy, vz = p.velocity
        ax, ay, az = p.acceleration
        vx += ax
        vy += ay
        vz += az
        px += vx
        py += vy
        pz += vz
        result.append(Particle((px, py, pz), (vx, vy, vz), (ax, ay, az)))
    return result


def part2(lines):
    """
    >>> part2(load_example(__file__, "20"))
    1
    """
    particles = prepare_data(lines)
    for _ in range(50):
        tbr = set()
        for p0, p1 in combinations(particles, 2):
            if p0.position == p1.position:
                tbr.add(p0.position)
        particles = [p for p in particles if p.position not in tbr]
        particles = simulate(particles)
    return len(particles)


if __name__ == "__main__":
    data = load_input(__file__, 2017, "20")
    print(part1(data))
    print(part2(data))
