package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day1(val lines: List<String>) : AocChallenge(2023, 1) {

    override fun part1(): Int {
        return lines.sumOf { line ->
            val first = line.first { it.isDigit() }.digitToInt()
            val last = line.last { it.isDigit() }.digitToInt()
            10 * first + last
        }
    }

    override fun part2(): Int {
        return -1
    }
}
