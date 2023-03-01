package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day1(val lines: List<String>) : AocChallenge(2019, 1) {

    fun getFuel(mass: Int): Int {
        return mass / 3 - 2
    }

    override fun part1(): Int {
        return lines.sumOf { getFuel(it.toInt()) }
    }

    fun getTotalFuel(mass: Int): Int {
        var m = getFuel(mass)
        var total = 0
        while (m > 0) {
            total += m
            m = getFuel(m)
        }
        return total
    }

    override fun part2(): Int {
        return lines.sumOf { getTotalFuel(it.toInt()) }
    }
}
