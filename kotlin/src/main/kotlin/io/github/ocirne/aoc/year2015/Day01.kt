package io.github.ocirne.aoc.year2015

import java.lang.RuntimeException

class Day01(lines: List<String>) {

    private val line = lines[0]

    fun part1(): Int {
        val counts = line.groupingBy { it }.eachCount()
        return counts.getOrDefault('(', 0) - counts.getOrDefault(')', 0)
    }

    fun part2(): Int {
        var floor = 0
        line.forEachIndexed { index, bracket -> run {
                if (bracket == '(')
                    floor++
                if (bracket == ')')
                    floor--
                if (floor < 0)
                    return index + 1
            }
        }
        throw RuntimeException()
    }
}
