package io.github.ocirne.aoc.year2019

import io.github.ocirne.aoc.AocChallenge

class Day5(val lines: List<String>) : AocChallenge(2019, 5) {

    override fun part1(): Int {
        return IntCodeEmulator2019(lines.first()).run(1).getDiagnosticCode()
    }

    override fun part2(): Int {
        return IntCodeEmulator2019(lines.first()).run(5).getDiagnosticCode()
    }
}
