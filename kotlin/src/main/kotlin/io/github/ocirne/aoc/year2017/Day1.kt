package io.github.ocirne.aoc.year2017

import io.github.ocirne.aoc.AocChallenge

class Day1(val lines: List<String>) : AocChallenge(2017, 1) {

    private fun toList(line: String): List<Int> {
        return line.map { Character.getNumericValue(it) }
    }

    fun solveCaptcha1(line: String): Int {
        val values = toList(line)
        val lineWrapped = values + values[0]
        return lineWrapped
            .zipWithNext { a, b -> if (a == b) a else 0 }
            .sum()
    }

    override fun part1(): Int {
        return solveCaptcha1(lines.first())
    }

    fun solveCaptcha2(line: String): Int {
        val values = toList(line)
        val valuesRotated = values.drop(values.size / 2) + values.take(values.size / 2)
        return values
            .zip(valuesRotated)
            .sumOf { (a, b) -> if (a == b) a else 0 }
    }

    override fun part2(): Int {
        return solveCaptcha2(lines.first())
    }
}
