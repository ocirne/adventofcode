package io.github.ocirne.aoc.year2021

import io.github.ocirne.aoc.AocChallenge

class Day1(lines: List<String>) : AocChallenge(2021, 1) {

    private val depths = lines.map { i -> i.toInt() }

    override fun part1(): Int {
        return depths.zipWithNext { a, b -> a < b }.count { it }
    }

    override fun part2(): Int {
        return depths
            .drop(2).indices
            .map { i -> depths.subList(i, i + 3).sum() }
            .zipWithNext { a, b -> a < b }
            .count { it }
    }
}
