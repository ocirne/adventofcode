package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day1(val lines: List<String>) : AocChallenge(2019, 1) {

    fun getFuel(mass: Int): Int {
        return mass / 3 - 2
    }

    override fun part1(): Int {
        return lines.sumOf { getFuel(it.toInt()) }
    }

    override fun part2(): Int {
        return 0
    }
}
