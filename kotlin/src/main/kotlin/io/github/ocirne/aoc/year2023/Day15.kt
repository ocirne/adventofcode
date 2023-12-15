package io.github.ocirne.aoc.year2023

import io.github.ocirne.aoc.AocChallenge

class Day15(val lines: List<String>) : AocChallenge(2023, 15) {

    fun aocHash(step: String): Int {
        return step.fold(0) { value, c -> (value + c.code) * 17 % 256 }
    }

    override fun part1(): Int {
        return lines.first().split(',').sumOf { step -> aocHash(step) }
    }

    override fun part2(): Int {
        return -1
    }
}
