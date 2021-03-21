package io.github.ocirne.aoc.year2018

import io.github.ocirne.aoc.AocChallenge

class Day1(private val lines: List<String>) : AocChallenge{

    override fun part1(): Int {
        return lines.map { it.toInt() }.sum()
    }

    override fun part2(): Any {
        return 0
    }
}