package io.github.ocirne.aoc.year2017

import io.github.ocirne.aoc.AocChallenge

class Day1(lines: List<String>) : AocChallenge(2017, 1) {

    private val line = lines[0].map { c -> Character.getNumericValue(c) }

    override fun part1(): Int {
        val lineWrapped = line + line[0]
        return lineWrapped
            .zipWithNext { a, b -> if (a == b) a else 0 }
            .sum()
    }

    override fun part2(): Int {
        val lineRotated = line.drop(line.size / 2) + line.take(line.size / 2)
        return line
            .zip(lineRotated)
            .map { (a, b) -> if (a == b) a else 0 }
            .sum()
    }
}
