package io.github.ocirne.aoc.year2022

import io.github.ocirne.aoc.AocChallenge

class Day4(val lines: List<String>) : AocChallenge(2022, 4) {

    override fun part1(): Int {
        return lines.count { line ->
            val (first, second) = line.split(',')
            val (f0, f1) = first.split('-').map { it.toInt() }
            val (s0, s1) = second.split('-').map { it.toInt() }
            (s0 <= f0 && f1 <= s1) || (f0 <= s0 && s1 <= f1)
        }
    }

    override fun part2(): Int {
        return -1
    }
}
