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

    override fun part2(): Int {
        return 42
    }
}
