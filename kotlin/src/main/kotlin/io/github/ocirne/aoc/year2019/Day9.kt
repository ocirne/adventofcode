package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day9(val lines: List<String>) : AocChallenge(2019, 9) {

    override fun part1(): Long {
        return IntCodeEmulator2019(lines.first()).run(1).getLastOutput()
    }

    override fun part2(): Long {
        return IntCodeEmulator2019(lines.first()).run(2).getLastOutput()
    }
}
