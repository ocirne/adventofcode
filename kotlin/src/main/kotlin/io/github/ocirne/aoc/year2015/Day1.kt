package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge
import java.lang.RuntimeException

class Day1(lines: List<String>) : AocChallenge {

    private val line = lines[0]

    override fun part1(): Int {
        return line.count { it == '(' } - line.count { it == ')' }
    }

    override fun part2(): Int {
        var floor = 0
        line.forEachIndexed { index, bracket ->
            run {
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
