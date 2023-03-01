package io.github.ocirne.aoc.year2018

import io.github.ocirne.aoc.AocChallenge

class Day1(private val lines: List<String>) : AocChallenge(2018, 1) {

    override fun part1(): Int {
        return lines.sumOf { it.toInt() }
    }

    override fun part2(): Any {
        TODO()
    }
}