package io.github.ocirne.aoc.year2015

import io.github.ocirne.aoc.AocChallenge
import java.lang.RuntimeException

class Day1(val lines: List<String>) : AocChallenge(2015, 1) {

    fun countBrackets(line: String): Int {
        return line.count { it == '(' } - line.count { it == ')' }
    }

    override fun part1(): Int {
        return countBrackets(lines[0])
    }

    fun findBasement(line: String): Int {
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

    override fun part2(): Int {
        return findBasement(lines[0])
    }
}
