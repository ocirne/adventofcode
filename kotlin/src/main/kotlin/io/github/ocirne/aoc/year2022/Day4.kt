package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge

class Day4(val lines: List<String>) : AocChallenge(2022, 4) {

    private val regex = """(\d+)-(\d+),(\d+)-(\d+)""".toRegex()

    private fun foo(line: String): List<Int> {
        return regex.find(line)!!.destructured.toList().map { it.toInt() }
    }

    override fun part1(): Int {
        return lines.count {
            val (f0, f1, s0, s1) = foo(it)
            (s0 <= f0 && f1 <= s1) || (f0 <= s0 && s1 <= f1)
        }
    }

    override fun part2(): Int {
        return lines.count {
            val (f0, f1, s0, s1) = foo(it)
            (f1 >= s0 && f0 <= s1) || (f1 <= s0 && f0 >= s1)
        }
    }
}
