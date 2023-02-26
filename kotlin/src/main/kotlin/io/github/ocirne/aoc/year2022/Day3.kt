package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge

class Day3(val lines: List<String>) : AocChallenge(2022, 3) {

    override fun part1(): Int {
        return lines.sumOf {
            val first = it.substring(0, it.length / 2).toSet()
            val second = it.substring(it.length / 2).toSet()
            val common = first.intersect(second).first()
            getPriority(common)
        }
    }

    override fun part2(): Int {
        return lines.chunked(3).sumOf {
            val first = it[0].toSet()
            val second = it[1].toSet()
            val third = it[2].toSet()
            val common = first.intersect(second).intersect(third).first()
            getPriority(common)
        }
    }

    private fun getPriority(c: Char): Int {
        return if (c.isUpperCase()) c - 'A' + 27 else c - 'a' + 1
    }
}
