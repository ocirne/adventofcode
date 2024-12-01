package io.github.ocirne.aoc.year2024

import io.github.ocirne.aoc.AocChallenge
import kotlin.math.abs

class Day1(val lines: List<String>) : AocChallenge(2024, 1) {

    private val whitespace = Regex("\\s+")

    private fun extractList(index: Int): List<Int> {
        return lines.map { line -> line.split(whitespace)[index].toInt() }.sorted()
    }

    private val leftList = extractList(0)
    private val rightList = extractList(1)

    override fun part1(): Int {
        return leftList.zip(rightList).sumOf { (l, r) -> abs(r - l) }
    }

    override fun part2(): Int {
        val rightCounts = rightList.groupingBy { it }.eachCount()
        return leftList.sumOf { x -> x * rightCounts.getOrDefault(x, 0) }
    }
}
