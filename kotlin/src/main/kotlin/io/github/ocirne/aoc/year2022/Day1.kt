package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge

class Day1(val lines: List<String>) : AocChallenge(2022, 1) {

    override fun part1(): Int {
        return sumCalories().maxOrNull()!!
    }

    override fun part2(): Int {
        return sumCalories().sorted().reversed().take(3).sum()
    }

    private fun sumCalories(): List<Int> {
        val indexOfNewLines = listOf(-1) +
                lines.mapIndexedNotNull { index, s -> index.takeIf { s.isEmpty() } } +
                listOf(lines.size)
        return indexOfNewLines.zipWithNext { fromIndex, toIndex ->
            val calories = lines.subList(fromIndex + 1, toIndex)
            calories.sumOf { i -> i.trim().toInt() }
        }
    }
}
