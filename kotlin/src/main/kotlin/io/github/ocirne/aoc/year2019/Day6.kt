package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day6(val lines: List<String>) : AocChallenge(2019, 6) {

    private val orbitsAround = lines.associate { line ->
        val (p, s) = line.split(')')
        s to p
    }

    fun countOrbits(o: String): Int {
        if (o == "COM") {
            return 0
        }
        return countOrbits(orbitsAround[o]!!) + 1
    }

    override fun part1(): Int {
        return orbitsAround.keys.sumOf { countOrbits(it) }
    }

    fun commonParent(you: String, san: String): String {
        var planets_you = mutableSetOf<String>()
        var py = you
        while (py != "COM") {
            planets_you.add(py)
            py = orbitsAround[py]!!
        }
        var ps = san
        while (!planets_you.contains(ps)) {
            ps = orbitsAround[ps]!!
        }
        return ps
    }

    override fun part2(): Int {
        val p = commonParent("YOU", "SAN")
        val y = countOrbits("YOU")
        val s = countOrbits("SAN")
        val b = countOrbits(p)
        return (y-b) + (s-b) - 2
    }
}
